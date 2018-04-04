import numpy as np

BSIZE_SP = 512 # Max size of a line of data; we don't want to read the
               # whole file to find a line, in case file does not have
               # expected structure.
               
MDATA_LIST = [b'title', b'date', b'plotname', b'flags', b'no. variables',
              b'no. points', b'dimensions', b'command', b'option']

def read(fname):
    """
    Read ngspice binary raw files. Return tuple of the data, and the
    plot metadata. 
    """
    fp = open(fname, 'rb')
    plot = {}   
    #count = 0
    while (True):
        try:
            mdata = fp.readline(BSIZE_SP).split(b':', maxsplit=1)
            
        except:
            raise
        if len(mdata) == 2:
            if mdata[0].lower() in MDATA_LIST:
                plot[mdata[0].lower()] = mdata[1].strip()
            
            # nacitanie metadat - zoznam premennych, typy, jednotky, pocet dat
            if mdata[0].lower() == b'variables':
                nvars = int(plot[b'no. variables'])
                npoints = int(plot[b'no. points'])
                plot['varnames'] = []
                plot['varunits'] = []
                
                for varn in range(nvars):
                    varspec = (fp.readline(BSIZE_SP).strip().decode('ascii').split())
                    assert(varn == int(varspec[0]))
                    plot['varnames'].append(varspec[1])
                    plot['varunits'].append(varspec[2])
                    
            if mdata[0].lower() == b'binary':
                rowdtype = np.dtype({'names': plot['varnames'],
                                     'formats': [np.complex_ if b'complex'
                                                 in plot[b'flags']
                                                 else np.float_]*nvars})
                                                 
                # nacitanie dat a ich konverzia na maticu, po transpozicii su data 
                # usporiadane podla premennych v riadkoch
                # @TODO - vyhladat efektivnejsi postup
                dt=[]
                q = np.fromfile(fp, dtype=rowdtype, count=npoints)
                for i in range(len(q)):
                    dt.append(list(q[i]))
                dt = (np.array(dt)).T
                
                # konverzia dat na slovnik data{'var_name'}: [values ...], ...}
                data={}
                for i in range(len(plot['varnames'])):
                    data[plot['varnames'][i]] = dt[:][i]

                fp.readline() # Read to the end of line
                
                plot[b'no. variables'] = int(plot[b'no. variables'])
                return data, plot
        else:
            # chybny format dat
            return {},{}
