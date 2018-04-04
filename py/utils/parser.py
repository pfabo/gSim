#!/usr/bin/env python
'''
B{gschem (*.sch, *.sym) file Python parser}

Trieda B{gschParser} je urcena pre extrahovanie elementov zo schemy alebo komponentu 
vytvoreneho programom  gschem podla 
U{dokumentacie<http://geda.seul.org/wiki/geda:file_format_spec>} k formatu suboru.

Parametrom konstruktora triedy je meno suboru schemy (*.sch) alebo komponentu (*.sym), 
metody triedy vracaju zoznam elementov zvoleneho typu. 

Parser vyuziva standarny modul pre spracovanie regulernych vyrazov.

I{Verzia}::

    090801 0.10 zakladna verzia
    090906 0.11 uprava pre nacitanie zlozenych atributov
    090919 0.12 uprava pre spolocne nacitanie parametrov *.sch a *.sym
    090920 0.13 doplnenie nacitanie atributov pinov
    091002 0.14 doplneny parser graficke komponenty
    091008 0.15 doplnene vyhladavanie atributov v textovych retazcoch
    091025 0.16 oprava duplicitneho oznacenia width v dokumentacii gEDA
    091222 0.17 uprava parsovania atributov \_
    
'''
# ----------------------------------------------------------------------

#!/usr/bin/env python
import fileinput, string, sys
import re

class gschParser():
    # ----------------------------------------------------------------------
    # Konstruktor a globalne premenne
    # ----------------------------------------------------------------------
    def __init__(self, fileName): 
        # Vseobecny nepovinny zoznam parametrov objektu
        # Uzatvoreny medzi {...}
        self.p_par=r'\n?({[\w\s\d=&+-_\\/\n \(\).?\[\]]+})?'
        
        # nacitanie suboru schemy alebo komponentu do textoveho pola
        file = open(fileName, "r")
        self.fileText = file.read() 
        file.close() 

    # ----------------------------------------------------------------------
    def component(self):
        '''
        Funkcia extrahuje standardne (referencovane) komponenty zo suboru schemy
        
        @return:
        Funkcia vrati zoznam asociativnych poli s prvkami komponentu zoradenymi 
        podla nazvu klucov uvedenych v specifikacii
        U{komponentu <http://geda.seul.org/wiki/geda:file_format_spec#component>}
        
        Doplnkove atributy, ak boli v subore schemy k elementu priradene, su 
        v navratovom zozname zaradene pod klucom I{'attributes'}.
        
        Navratovy zoznam ma format
        
        I{[ { 'x'=..., 'y'=..., ... 'attributes'=[{attr1}, {attr2} ...] },  ... ]}
        '''
        # Navratova hodnota
        cmpList=[]
        
        # Pattern pre zahlavie komponentu
        # C x y selectable angle mirror basename
        p_cmp=r'(?:c|C\s+)([-\d]+)\s+([-\d]+)\s+(\d+)\s+(\d+)\s+(\d+)\s+([_a-zA-Z0-9\-]+\.[a-zA-Z]+)\s+\n?'
        
        for m in re.finditer(p_cmp+self.p_par, self.fileText):
            attr={}
            
            attrParam=m.groups()
            attr['x']         =int(attrParam[0])
            attr['y']         =int(attrParam[1])
            attr['select']    =int(attrParam[2])
            attr['angle']     =int(attrParam[3])
            attr['mirror']    =int(attrParam[4])
            attr['basename']  =attrParam[5]
            attr['attributes']=self.attributeParser(m.groups()[6])
            
            cmpList.append(attr)
        return cmpList
    # ----------------------------------------------------------------------
    def text(self):
        '''
        Funkcia extrahuje textove objekty zo suboru schemy okrem textov, 
        ktore su atributmi objektov
        
        @return:
        Funkcia vrati zoznam asociativnych poli s prvkami textov zoradenymi 
        podla nazvu klucov uvedenych v specifikacii
        U{textu <http://geda.seul.org/wiki/geda:file_format_spec#line>}
        
         
        Navratovy zoznam ma format
        
        I{[ { 'x'=..., 'y'=..., ... }}
        '''
        
        # Navratova hodnota
        textList=[]
        
        schTmp=self.fileText    # lokalna kopia 
        # odstranenie blokov s atributmi
        schTmp=re.sub(r'\n?{[\w\s\d=+-\\/\n \(\).?\[\]]+}', '', schTmp)
        
        # vyhladanie textovych objektov
        # T x y color size visibility show_name_value angle alignment num_lines
        p_text=r'(?:t|T)\s+([-\d]+)\s+([-\d]+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+\n?([ &+-?\w\d\-_., :=\(\)\[\]]+)\n?'
        
        # prehladanie retazca, vyhladanie zahlavia atributu
        for m in re.finditer(p_text, schTmp):

            attr={}
            # m.end() vrati koniec najdenej vorky
            # m.groups() vrati zoznam parametrov atributu
            attrParam=m.groups()
            
            # vyhladanie viacriadkoveho textu
            str_next=''
            if int(attrParam[8])!=1:
                x=re.search(r'[&+-?\w\d\-_., :=\(\)\[\]]+\n'*(int(attrParam[8])-1),schTmp[m.end():])
                str_next='\n'+x.group(0)
            
            # priradenie hodnot parametrom atributu
            attr['x']         =int(attrParam[0])
            attr['y']         =int(attrParam[1])
            attr['color']     =int(attrParam[2])
            attr['size']      =int(attrParam[3])
            attr['visibility']=int(attrParam[4])
            attr['show']      =int(attrParam[5])
            attr['angle']     =int(attrParam[6])
            attr['alignment'] =int(attrParam[7])
            attr['lines']     =int(attrParam[8])
            
            attr['text']=attrParam[9]+str_next
            
            textList.append(attr)
        
        return textList
    # ----------------------------------------------------------------------
    def line(self):
        '''
        Funkcia extrahuje ciary (graficke komponenty) zo suboru schemy
        
        @return:
        Funkcia vrati zoznam asociativnych poli s prvkami ciar zoradenymi 
        podla nazvu klucov uvedenych v specifikacii
        U{ciary <http://geda.seul.org/wiki/geda:file_format_spec#line>}
        
        Doplnkove atributy, ak boli v subore schemy k ciare priradene, su 
        v navratovom zozname zaradene pod klucom I{'attributes'}.
         
        Navratovy zoznam ma format
        
        I{[ { 'x1'=..., 'y1'=..., ... 'attributes'=[{attr1}, {attr2} ...] },  ... ]}
        '''
        # Navratova hodnota
        lineList=[]
        
        # Pattern pre vseobecnu ciaru v scheme
        # L x1 y1 x2 y2 color width capstyle dashstyle dashlength dashspace
        p_line=r'(?:l|L)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+\n?'
        
        for m in re.finditer(p_line+self.p_par, self.fileText):
            attr={}
            
            attrParam=m.groups()
            attr['x1']         =int(attrParam[0])
            attr['y1']         =int(attrParam[1])
            attr['x2']         =int(attrParam[2])
            attr['y2']         =int(attrParam[3])
            attr['color']      =int(attrParam[4])
            attr['width']      =int(attrParam[5])
            attr['capstyle']   =int(attrParam[6])
            attr['dashstyle']  =int(attrParam[7])
            attr['dashlength'] =int(attrParam[8])
            attr['dashspace']  =int(attrParam[9])
            attr['attributes'] =self.attributeParser(m.groups()[10])
            
            lineList.append(attr)
            
        return lineList
    # ----------------------------------------------------------------------
    def circle(self):
        '''
        Funkcia extrahuje kruznice zo suboru schemy
        
        @return:
        Funkcia vrati zoznam asociativnych poli s prvkami kruznice zoradenymi 
        podla nazvu klucov uvedenych v specifikacii
        U{kruznice <http://geda.seul.org/wiki/geda:file_format_spec#circle>}
        
        Doplnkove atributy, ak boli v subore schemy ku kruznici priradene, su 
        v navratovom zozname zaradene pod klucom I{'attributes'}.
         
        Navratovy zoznam ma format
        
        I{[ { 'x'=..., 'y'=..., ... 'attributes'=[{attr1}, {attr2} ...] },  ... ]}
        '''
        # Navratova hodnota
        circleList=[]
        
        # Pattern pre vseobecnu ciaru v scheme
        # V x y radius color width capstyle dashtype dashlength dashspace filltype 
        #       fillwidth angle1 pitch1 angle2 pitch2
        p_circ=         r'(?:v|V)\s+(-?\d+)\s+(-?\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s'
        p_circ=p_circ +           '+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s'
        p_circ=p_circ +           '+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+\n?'
        
        for m in re.finditer(p_circ+self.p_par, self.fileText):
            attr={}
            
            attrParam=m.groups()
            attr['x']          =int(attrParam[0])
            attr['y']          =int(attrParam[1])
            attr['radius']     =int(attrParam[2])
            attr['color']      =int(attrParam[3])
            attr['width']      =int(attrParam[4])
            attr['capstyle']   =int(attrParam[5])
            attr['dashstyle']  =int(attrParam[6])
            attr['dashlength'] =int(attrParam[7])
            attr['dashspace']  =int(attrParam[8])
            attr['filltype']   =int(attrParam[9])
            attr['fillwidth']  =int(attrParam[10])
            attr['angle1']     =int(attrParam[11])
            attr['pitch1']     =int(attrParam[12])
            attr['angle2']     =int(attrParam[13])
            attr['pitch2']     =int(attrParam[14])
            attr['attributes'] =self.attributeParser(m.groups()[15])
            
            circleList.append(attr)
        return circleList
        
    # ----------------------------------------------------------------------
    def arc(self):
        '''
        Funkcia extrahuje kruhove obluky zo suboru schemy
        
        @return:
        Funkcia vrati zoznam asociativnych poli s prvkami kruhovych oblukov zoradenymi 
        podla nazvu klucov uvedenych v specifikacii
        U{kruznice <http://geda.seul.org/wiki/geda:file_format_spec#arc>}
        
        Doplnkove atributy, ak boli v subore schemy ku kruznici priradene, su 
        v navratovom zozname zaradene pod klucom I{'attributes'}.
         
        Navratovy zoznam ma format
        
        I{[ { 'x'=..., 'y'=..., ... 'attributes'=[{attr1}, {attr2} ...] },  ... ]}
        '''
        # Navratova hodnota
        arcList=[]
        
        # Pattern pre vseobecnu ciaru v scheme
        # A x y radius startangle sweepangle color width capstyle dashtype dashlength dashspace
        p_arc=         r'(?:a|A)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s'
        p_arc=p_arc +            '+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s'
        p_arc=p_arc +            '+(-?\d+)\s+\n?'
        
        for m in re.finditer(p_arc+self.p_par, self.fileText):
            attr={}
            
            attrParam=m.groups()
            attr['x']          =int(attrParam[0])
            attr['y']          =int(attrParam[1])
            attr['radius']     =int(attrParam[2])
            attr['startangle'] =int(attrParam[3])
            attr['sweepangle'] =int(attrParam[4])
            attr['color']      =int(attrParam[5])
            attr['width']      =int(attrParam[6])
            attr['capstyle']   =int(attrParam[7])
            attr['dashstyle']  =int(attrParam[8])
            attr['dashlength'] =int(attrParam[9])
            attr['dashspace']  =int(attrParam[10])
            attr['attributes'] =self.attributeParser(m.groups()[11])
            
            arcList.append(attr)
        return arcList
    # ----------------------------------------------------------------------
    def box(self):
        '''
        Funkcia extrahuje obdlzniky zo suboru schemy.
        
        @return:
        Funkcia vrati zoznam asociativnych poli s prvkami boxu zoradenymi 
        podla nazvu klucov uvedenych v specifikacii
        U{boxu <http://geda.seul.org/wiki/geda:file_format_spec#box>}
        
        Doplnkove atributy, ak boli v subore schemy k boxu priradene, su 
        v navratovom zozname zaradene pod klucom I{'attributes'}.
         
        Navratovy zoznam ma format
        
        I{[ { 'x'=..., 'y'=..., ... 'attributes'=[{attr1}, {attr2} ...] },  ... ]}
        '''
        # Navratova hodnota
        boxList=[]
        
        p_box=         r'(?:b|B)\s+(-?\d+)\s+(-?\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s'
        p_box=p_box +            '+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s'
        p_box=p_box +            '+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+\n?'
        
        for m in re.finditer(p_box+self.p_par, self.fileText):
            
            attr={}
            
            attrParam=m.groups()

            attr['x']          =int(attrParam[0])
            attr['y']          =int(attrParam[1])
            attr['width']      =int(attrParam[2])
            attr['height']     =int(attrParam[3])
            attr['color']      =int(attrParam[4])
            attr['linewidth']  =int(attrParam[5])
            attr['capstyle']   =int(attrParam[6])
            attr['dashstyle']  =int(attrParam[7])
            attr['dashlength'] =int(attrParam[8])
            attr['dashspace']  =int(attrParam[9])
            attr['filltype']   =int(attrParam[10])
            attr['fillwidth']  =int(attrParam[11])
            attr['angle1']     =int(attrParam[12])
            attr['pitch1']     =int(attrParam[13])
            attr['angle2']     =int(attrParam[14])
            attr['pitch2']     =int(attrParam[15])
            attr['attributes'] =self.attributeParser(m.groups()[16])
            
            boxList.append(attr)
        return boxList
    # ----------------------------------------------------------------------
    def version(self):
        '''
        Funkcia extrahuje verziu a typ suboru zo suboru schemy
        
        @return:
        Funkcia vrati asociativne pole s prvkami
        podla nazvu klucov uvedenych v specifikacii
        U{verzie suboru <http://geda.seul.org/wiki/geda:file_format_spec#version>}
        
        Navratove asociativne pole ma format
        
        I{ {'version'=..., 'fileformat_version'=... }}
        '''
        #  v version fileformat_version
        p_version=r'(?:v|V)\s+(\d+)\s+(\d)\s+\n?'
        m=re.search(p_version,self.fileText).groups()
        
        attr={}
        attr['version']=m[0]
        attr['fileformat_version']=m[1]
        
        return attr

    # ----------------------------------------------------------------------
    def net(self):
        '''
        Funkcia extrahuje prepojenia (spoje) zo suboru schemy
        
        @return:
        Funkcia vrati zoznam asociativnych poli s prvkami prepojenia zoradenymi 
        podla nazvu klucov uvedenych v specifikacii
        U{prepojenia <http://geda.seul.org/wiki/geda:file_format_spec#net>}
        
        Doplnkove atributy, ak boli v subore schemy k elementu priradene, su 
        v navratovom zozname zaradene pod klucom I{'attributes'}.
        
        Navratovy zoznam ma format
        
        I{[ { 'x1'=..., 'y1'=..., ... 'attributes'=[{attr1}, {attr2} ...] },  ... ]}
        '''
        # Navratova hodnota
        netList=[]
        
        # Pattern pre prepojenie v scheme
        # N x1 y1 x2 y2 color 
        p_net=r'(?:n|N)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+\n?'
        
        for m in re.finditer(p_net+self.p_par, self.fileText):
            attr={}
            
            attrParam=m.groups()
            attr['x1']         =int(attrParam[0])
            attr['y1']         =int(attrParam[1])
            attr['x2']         =int(attrParam[2])
            attr['y2']         =int(attrParam[3])
            attr['color']      =int(attrParam[4])
            attr['attributes']=self.attributeParser(m.groups()[5])
            
            netList.append(attr)
            
        return netList
    # ----------------------------------------------------------------------
    def pin(self):
        '''
        Funkcia extrahuje udaje o pinoch komponentu zo suboru schemy
        
        @return:
        Funkcia vrati zoznam asociativnych poli s prvkami pinov zoradenymi 
        podla nazvu klucov uvedenych v specifikacii k
        U{pinu <http://geda.seul.org/wiki/geda:file_format_spec#pin>}
        
        Atributy pinu su v navratovom zozname zaradene pod klucom I{'attributes'}.
        
        Navratovy zoznam ma format
        
        I{[ { 'x1'=..., 'y1'=..., ... 'attributes'=[{attr1}, {attr2} ...] },  ... ]}
        '''
        # Navratova hodnota
        pinList=[]
        
        # Pattern pre zahlavie pinu
        # P x y selectable angle mirror basename
        p_pin=r'(?:p|P\s+)(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d)\s+(\d)\s+\n?'
        
        for m in re.finditer(p_pin+self.p_par, self.fileText):
            attr={}
            
            attrParam=m.groups()
            attr['x1']        =int(attrParam[0])
            attr['y1']        =int(attrParam[1])
            attr['x2']        =int(attrParam[2])
            attr['y2']        =int(attrParam[3])
            attr['color']     =int(attrParam[4])
            attr['pintype']   =attrParam[5]
            attr['whichend']  =attrParam[6]
            attr['attributes']=self.attributeParser(m.groups()[7])
            pinList.append(attr)
            
        return pinList
    # ----------------------------------------------------------------------
    def attrValue(self,attrName):
        '''
        Funkcia skontroluje textove retazce komponentu, vyhlada retazce 
        zapisane v tvare attribute=value a vrati hodnotu zadaneho stributu
        '''
        p_list=self.text()
        for q in p_list:
            x=re.search(r'([.\w\d]+)=([+-?&\w\d\-_., :=\(\)\[\]]+)',q.get('text'))
            if x!=None:
                if x.groups()[0] == attrName:
                    return x.groups()[1]
        return 'undefined'
    
    # ----------------------------------------------------------------------
    def attribute(self):
        '''
        Funkcia vrati asociativne pole s hodnotami atributov komponentu/schemy 
        extrahovanych z textovych retazcov zadanych v tvare meno=hodnota.
        '''
        a_list={}
        for t in self.text():
            x=re.search(r'([.\w\d&_]+)=([ +-?\w\d\-_., :=\(\)\[\]]+)',t.get('text'))
            if x!=None:
                a_list[x.groups()[0]]=x.groups()[1]
                
        return a_list
    # ----------------------------------------------------------------------
    # Pomocne funkcie
    # ----------------------------------------------------------------------
    def attributeParser(self,attrString):
        '''
        Pomocna funkcia extrahuje atributy uzatvorene v bloku ohranicenom zatvorkami {}
        
        Funkcia predpoklada format atributov v tvare jednoriadkoveho textu
        
        I{T x y color size visibility show_name_value angle alignment num_lines}
        
        I{attr=value}
        
        @return:
        Funkcia vrati zoznam nacitanych atributov v tvare asociativneho pola,
        mena klucov pola zodpovedaju oznaceniu podla specifikacie 
        U{atributu <http://geda.seul.org/wiki/geda:file_format_spec#attributes>}
        
        I{[{'x'=...,'y'=...,'color'=..., ...}, {...} ]}
        '''
        # navratova hodnota
        attrList={}
        
        if attrString==None:
            return attrList
        
        # pattern pre textove zahlavie atributu
        # T x y color size visibility show_name_value angle alignment num_lines
        p_attrText=r'(?:T)\s+([-\d]+)\s+([-\d]+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+\n?'
        
        # prehladanie retazca, vyhladanie zahlavia atributu
        for m in re.finditer(p_attrText, attrString):
            attr={}
            # m.end() vrati koniec najdenej vorky
            # m.groups() vrati zoznam parametrov atributu
            attrParam=m.groups()
            
            if int(attrParam[8])!=1:
                print ('Error - Number of lines > 1 in attribute definition')
                return []
            
            # priradenie hodnot parametrom atributu
            attr['x']         =int(attrParam[0])
            attr['y']         =int(attrParam[1])
            attr['color']     =int(attrParam[2])
            attr['size']      =int(attrParam[3])
            attr['visibility']=int(attrParam[4])
            attr['show']      =int(attrParam[5])
            attr['angle']     =int(attrParam[6])
            attr['alignment'] =int(attrParam[7])
            attr['lines']     =int(attrParam[8])
            
            # vyhladanie a rozlozenie hodnoty atributu
            tmp=attrString[m.end():]
            x=re.search(r'([.\w\d]+)=([+-?&\w\d\-_\\., :=\(\)\[\]]+)\n',tmp)
            attr['name']=x.groups()[0]
            attr['data']=x.groups()[1]

            attrList[attr.get('name')]=attr
            del attr['name']    # redunantna hodnota, meno atributu je klucom
        return  attrList
# ----------------------------------------------------------------------

if __name__ == '__main__':
    '''
    Test pouzitia - vypis komponentov zo suboru *.sch a/alebo parametrov
    pinov zo suboru *.sym.
    
    python gschParser.py meno_suboru.sch/sym
    '''
    
    parser=gschParser(sys.argv[1])
    
    print ('List of components')
    p_list=parser.component()
    for q in p_list:
        attr=q.get('attributes') 
        print ('component ',q.get('x'),q.get('y'),q.get('basename') , attr.get('refdes',{}).get('data'))
    print ()
            
    print ('List of nets')
    p_list=parser.net()
    for q in p_list:
        attr=q.get('attributes') 
        print ('net       ',q.get('x1'),q.get('y1'), attr.get('netname',{}).get('data'))
    print ()
            
    print ('List of pins')
    p_list=parser.pin()
    for q in p_list:
        attr=q.get('attributes') 
        print ('pin       ',attr.get('pinnumber').get('data'),attr.get('pinlabel').get('data'))
    print ()
    
    print ('List of circles x,y,radius')
    p_list=parser.circle()
    for q in p_list:
        print ('circle    ',q.get('x'),q.get('y'),q.get('radius'))
    print ()
    
    print ('List of arcs x,y,startangle')
    p_list=parser.arc()
    for q in p_list:
        print ('arc      ',q.get('x'),q.get('y'),q.get('startangle'))
    print ()
    
    print ('List of lines x1,y1,x2,y2')
    p_list=parser.line()
    for q in p_list:
        print ('line     ',q.get('x1'),q.get('y1'),q.get('x2'),q.get('y2'))
    print ()
    
    print ('List of boxes x,y,w,h')
    p_list=parser.box()
    for q in p_list:
        print ('box       ',q.get('x'),q.get('y'),q.get('width'),q.get('height'))
    print ()
        
    print ('List of text objects x,y,text')
    p_list=parser.text()
    for q in p_list:
        print ('text      ',q.get('x'),q.get('y'),q.get('text'))
        
    print ('Object attributes')
    print ('RefDes = ',parser.attrValue('refdes'))
    print ('Device = ',parser.attrValue('device'))
    print ('Value  = ',parser.attrValue('value'))

#=======================================================================

