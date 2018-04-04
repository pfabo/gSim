#!/usr/bin/env python
'''
Trieda prehladava subor *.net po riadkoch, pri najdeni definicie komponentu
vyhlada prislusny *.sym komponent z kniznice a doplni/konvertuje parametre

'''
import types, errno
import os, fileinput, string, sys, re

from config import *
from utils import *

from xspice.analog import *
from xspice.digital import *
from xspice.mixed import *
from xspice.user import *


class ConvertNetlist():
    
    def __init__(self, netlist, c_list=None): 
        ''' 
        Konstruktor triedy pre konverziu netlistu.
        
        @param netlist:
            Meno vstupneho suboru netlistu (bez pripony *.net)
            
        @param c_list:
            Zoznam komponentov zapojenia, extrahovanych zo suboru schemy (*.sch),
            obsahuje atributy komponentov, ktore sa budu doplnat do netlistu.
        '''
        self.netlist = netlist
        self.modelDict={}       # zoznam pouzitych modelov komponentov a ciest k nim,
                                # zabranuje opakovanemu include rovnakeho modelu
        
        self.cmpList=c_list     # zoznam komponentov suboru
        
        # vyber cesty ku knizniciam podla suboru gafrc v pracovnom adresari
        # prida relativnu cestu k premennym config.PATH_SYM a config.PATH_MODEL
        try:
            path=os.getcwd()
            gafrc=open('./gafrc',"r")
            while 1:
                line = gafrc.readline( )
                
                if not line: break
                
                if line.find('component-library') > -1:
                    line=line.lstrip(' (')
                    line=line.rstrip(') \n')
                    data=line.split(' ')
                    data[1]=data[1].lstrip('\"')
                    data[1]=data[1].rstrip('\"')
                    n=data[1].find(config.PATH_SYM)
                    
                    config.PATH_SYM=data[1][0:n] + config.PATH_SYM
                    config.PATH_MODEL=data[1][0:n] + config.PATH_MODEL
                    break
            gafrc.close()
            
        except :
            print ('Error: gafrc file is not present in current working directory')
            exit(errno.ENOENT)

    def findSymbolFile(self, s_name):
        '''
        Vyhladanie suboru so symbolom komponentu. Adresare kniznice su definovane
        v subore gafrc, parameter symbol-library.
        '''
        fn=config.PATH_SYM
        file_list = []
        for root, dirs, files in os.walk(fn):
            for f in files:
                file_path = os.path.join(root, f)
                # striktne dodrzanie mena symbolu ../aaa.sym, vylucenie ../bb-aaa.sym
                # TODO - upravit
                if file_path.endswith('/'+s_name.lower()+'.sym'):
                    file_list.append(file_path)
                    
        if len(file_list) == 0:
            #print ('Error: Symbol ' + s_name + '.sym nenajdeny')
            return None
            
        if len(file_list) > 1:
            print ('Warning: Najdene duplicitne symboly ' + s_name + '.sym'  + '\n' + str(file_list))

        return file_list[0]

    def findModelFile(self, m_name):
        '''
        Vyhladanie suboru s modelom komponentu.
        
        Funkcia najprv hlada model v adresari projektu, potom v kniznici. 
        Lokalny model ma prioritu pred globalnym.
        
        Urcenie typu modelu, ak obsahuje .SUBCKT, model je kompozitny a 
        komponent bude v mene obsahovat X 
        '''
        fn=config.PATH_MODEL
        file_list = []
        
        # prehladanie adresaru s kniznicou modelov
        for root, dirs, files in os.walk(fn):
            for f in files:
                file_path = os.path.join(root, f)
                if file_path.endswith(m_name.lower()+'.sm'):
                    file_list.append(file_path)
                        
        if len(file_list) == 0:
            print ('Error: Model ' + m_name + '.sm nenajdeny')
            exit()
            
        if len(file_list) > 1:
            print ('Warning: Duplicitne modely ' + m_name + '.sm')
                
        fp = open(file_list[0], "r")
        lines = fp.readlines()
        fp.close()
        
        for s in lines:
            if s[0] != '*' and s.upper().find('.SUBCKT') >= 0:
                return file_list[0], 'SUBCKT' 

        return file_list[0], 'MODEL'
        
    def update(self):
        '''
        Nacita zo vstupneho po riadkoch netlist zapojenia. Pre najdene zname prefixy 
        komponentov vyvola metodu, ktora pre dany typ komponentu vyhlada jeho 
        subor *.sym a doplni model komponentu. 
        
        Rozpoznava prefixy D,Q,M,J,K,X,A, ostatne riadky zapisuje bez zmeny
        do vystupneho suboru.
        
        Vrati zoznam doplnenych modelov.
        '''
        try:
            inputFile = open(self.netlist+'.net', "r")
            self.lines = inputFile.readlines()
            inputFile.close() 
        except:
            print ('gnetConvert: Error open netlist file : ' + netlist + '.net')
            exit(errno.ENOENT)
            
        try:
            self.outputFile=open(self.netlist+'.net',"w")
        except:
            print ('gnetConvert: Error write netlist file : ' + netlist + '.net')
            exit(errno.ENOENT)
        
        for s in self.lines:
            q = None
            
            # dioda 
            # D<name> NA NK DNAME 
            if re.match(r'D[\w]+\s[-_+\d\w]+\s[-_+\d\w]+\s[\w]+', s)is not None:
                q=self.D(s)
        
            # npn, pnp bipolarny tranzistor
            # Q<name> NC NB NE QNAME
            if re.match(r'Q[\w]+\s[-_+\d\w]+\s[-_+\d\w]+\s[-_+\d\w]+\s[\w]+', s) is not None:
                q=self.Q(s)
            
            # mosfet tranzistor
            # M<name> ND NG NS MNAME
            if re.match(r'M[\w]+\s[-_+\d\w]+\s[-_+\d\w]+\s[-_+\d\w]+\s[\w]+', s) is not None:
                q=self.M(s)
                
            # jfet tranzistor
            # J<name> ND NG NS JNAME
            if re.match(r'J[\w]+\s[-_+\d\w]+\s[-_+\d\w]+\s[-_+\d\w]+\s[\w]+', s) is not None:
                q=self.J(s)
            
            # vzajomna indukcnost, vzduchovy transformator
            # K<name> NL1A NL1B NL2A NL2B MNAME
            if re.match(r'K[\w]+\s',s) is not None: 
                q=self.K(s)
            
            # vnoreny blok
            # X<name> N1 N2 N3 ... XNAME
            if re.match(r'X[\d\w]+\s',s) is not None: 
                q=self.X(s)
            
            # komponenty XSPICE
            if re.match(r'A[\w]+\s', s) is not None:
                q=self.A(s)
                
            # zapis do suboru
            if q is None:   
                self.outputFile.write(s)        # riadok bez zmeny
            else:
                #self.outputFile.write('\n')
                #self.outputFile.write('* '+s)    # zmena riadku
                self.outputFile.write(q)  #+'\n')
            
        self.outputFile.close()
        
        return self.modelDict
           
    def D(self,spice_diode):    
        '''
        Vyhlada a doplni model diody .INCLUDE cesta\...\model.sm
        '''
        q = spice_diode.split()                 
        model, _ = self.findModelFile(q[3]) # q[3] - diode (typ) name
        
        if q[3] in self.modelDict.keys():   # multiple include
            return spice_diode + '\n'
        else:
            self.modelDict[q[3]] = model
            return spice_diode + '\n.INCLUDE ' + model + '\n'
        
    def Q(self,spice_transistor):    
        '''
        Vyhlada a doplni model pnp/npn tranzistora .INCLUDE cesta\...\model
        '''
        q = spice_transistor.split()        # q[4] - transistor (typ) name
        model, _ = self.findModelFile(q[4])
        
        if q[4] in self.modelDict.keys():   # multiple include
            return spice_transistor # + '\n'
        else:
            self.modelDict[q[4]] = model
            return spice_transistor + '.INCLUDE ' + model + '\n'
    
    def J(self, spice_jfet):    
        '''                
        Vyhlada a doplni model j-fet tranzistora .INCLUDE cesta\...\model
        
        '''
        q = spice_jfet.split()  
        model, _ = self.findModelFile(q[4])
        
        if q[4] in self.modelDict.keys():   # multiple include
            return spice_jfet + '\n'
        else:
            self.modelDict[q[4]] = model
            return spice_jfet + '\n.INCLUDE ' + model + '\n'
    

    def M(self,spice_mos):    
        '''
        Doplni hodnotu pre uzol substrate(=source)
        Vyhlada a doplni model n/p mos .INCLUDE cesta\...\model
        '''
        
        q=spice_mos.split()
        m_name = q[4]
        q.append(0)                   # doplnenie uzla substratu
        q[5]= q[4]                      
        q[4]= q[3] 

        model, _ = self.findModelFile(m_name)
        
        retStr=''                     # navratovy string
        for i in q:                     
            retStr=retStr + i + ' '   
    
        if m_name in self.modelDict.keys():
            return retStr + '\n'
        else:
            self.modelDict[m_name] = model
            return retStr + '\n.INCLUDE ' + model + '\n'

    def X(self,xcomp): 
        '''
        Pre zname typy komponentov upravi poradie vyvodov podla standardnej deficie.
        Rozpoznava komponenty OP|OPAMP - nie je standardnym komponentom Spice/Xspice
        
        Doplni .INCLUDE modelu bloku
        '''
        xcomp = xcomp.rstrip('\r\n')
        q=xcomp.split()
        x_name = q[-1]
        
        symbol = self.findSymbolFile(x_name)
        cmpData=parser.gschParser(symbol)

        # blokovy model OPAMP operacneho zosilnovaca
        if re.match(r'OP|OPAMP', cmpData.attrValue('device').upper() )!=None:
            # pripojenie  OPAMP podla mien pinov
            q=self.X_OPAMP(q)
        
        model, _ = self.findModelFile(x_name)  
        
        # uprava hodnot atributov podla ich zmien v *.sch subore 
        # na zaklade refDes komponentu
        attrList=cmpData.attribute() 
        attrList=self.updateAttributes(attrList, q[0])
        
        parString = ' '
        if attrList['device'] == 'XYCE':
            try:
                del attrList['value']
                del attrList['description']
                del attrList['refdes']
                del attrList['device']
            except:
                pass
        
            parString = ' PARAMS: '
            for k in attrList.keys():
                parString = parString + k + "=" + attrList[k] + ' '
        
        if x_name in self.modelDict.keys():
            return xcomp + parString + '\n'
        else:
            self.modelDict[x_name] = model
            return xcomp + parString + '\n.INCLUDE ' + model +'\n'
    
    
    def A(self, spice_xspice):
        '''
        Konverzia komponentov s prikazmi riadenia simulacie a komponentov
        rozsireneho typu simulacie XSPICE. 
        Definicia standardnych komponentov je uvedena 
        v 'XSPICE Software User's Manual'
        '''
        q=spice_xspice.split()    
        symbol = self.findSymbolFile(q[-1])

        # nacitanie struktury komponentu
        cmpData=parser.gschParser(symbol)

        # default hodnoty atrbutov z definicie komponenty v *.sym subore        
        attrList=cmpData.attribute() 

        # uprava hodnot atributov podla ich zmien v *.sch subore 
        # na zaklade refDes komponentu
        attrList=self.updateAttributes(attrList, q[0])

        # Konverzie standardneho zapisu Spice na bloky XSPICE
        rtStr = ''                
        rtStr = XSPICE_User(q,cmpData, attrList)
        if rtStr != '': 
            return rtStr + '\n'
        
        rtStr=XSPICE_Digital(q,cmpData, attrList)
        if rtStr != '': 
            return rtStr + '\n'
        
        rtStr=XSPICE_Mixed(q,cmpData, attrList)
        if rtStr != '': 
            return rtStr + '\n'
        
        rtStr=XSPICE_Analog(q,cmpData, attrList)
        if rtStr != '': 
            return rtStr + '\n'
                
        return '* '+s
        
    def K(self, spice_transf):    
        '''
        Funkcia konvertuje riadok s parametrami transformatora na
        dve cievky previazane vzajomnou indukcnostou
        '''
        q = spice_transf.split()                       # rozdelenie retazca
        
        # vyhladanie komponentu schemy a kniznice
        symbol = self.findSymbolFile('transformer')

        # nacitanie struktury komponentu
        cmpData=parser.gschParser(symbol)
        
        # default hodnoty atrbutov z definicie komponenty v *.sym subore        
        attrList=cmpData.attribute() 
        
        # uprava hodnot atributov podla ich zmien v *.sch subore na zaklade 
        # refDes komponentu
        attrList=self.updateAttributes(attrList, q[0])
        
        # vytvorenie navratovej struktury
        rtStr=''
        rtStr=rtStr+'L1'+q[0]+' '+q[1]+' '+q[2]+' '+attrList.get('L1')+'\n'
        rtStr=rtStr+'L2'+q[0]+' '+q[3]+' '+q[4]+' '+attrList.get('L2')+'\n'
        rtStr=rtStr+q[0]+' L1'+q[0]+' L2'+q[0]+' '+q[5]+'\n'
        return rtStr + '\n'

        
    def X_OPAMP(self, q):
        '''
        Pomocna funkcia - vyhlada a vymeni uzly operacneho zosilnovaca
        '''
        # vyhladanie komponentu schemy a nacitanie pinov
        symbol = self.findSymbolFile(q[-1])

        cmpData=parser.gschParser(symbol)   # nacitanie struktury komponentu
        pinList=cmpData.pin()           # nacitanie zoznamu pinov komponentu
    
        # vyhladanie pinov podla skutocnych mien pinov
        temp=['0','0','0','0','0']
        retQ=['0','0','0','0','0','0','0']  
        
        for w in pinList:
            attr=w.get('attributes')
            data=attr['pinlabel']['data'].upper()
            if re.match(r'IN\-',data)!=None:
                n=int(attr['pinnumber']['data'])
                temp[1]=q[n]
            
            if re.match(r'IN\+',data)!=None:
                n=int(attr['pinnumber']['data'])
                temp[0]=q[n]
                
            if re.match(r'VCC\+',data)!=None:
                n=int(attr['pinnumber']['data'])
                temp[2]=q[n]
            
            if re.match(r'VCC\-',data )!=None:
                n=int(attr['pinnumber']['data'])
                temp[3]=q[n]
                
            if re.match(r'VSS',data)!=None:
                n=int(attr['pinnumber']['data'])
                temp[3]=q[n]
            
            if re.match(r'OUT',data)!=None:
                n=int(attr['pinnumber']['data'])
                temp[4]=q[n]
        
        retQ[0]=q[0]
        retQ[1]=temp[0]
        retQ[2]=temp[1]
        retQ[3]=temp[2]
        retQ[4]=temp[3]
        retQ[5]=temp[4]
        retQ[6]=q[-1]
        
        return retQ
   
    def updateAttributes(self, attrList, netRefdes):
        '''
        Zmena default hodnot atributov podla ich aktualnych hodnot v zapojeni.
        Pouziva sa pre zmenu vlastnosti komponentov typu 'A', hodnota atributu zadana
        v scheme prekryva default hodnotu z definicie komponentu.
        ''' 
        for i in self.cmpList:
            if i.get('attributes',{}).get('refdes',{}).get('data',{})==netRefdes:
                attr=i.get('attributes')
                for k in attr.keys():
                    attrList[k]=attr.get(k).get('data')
        return attrList
                    
    def addString(self, cmd):
        '''
        Pridanie povelu na koniec suboru, pred prikaz .END
        '''
        try:
            fp= open(self.netlist+'.net', "r")
            txt = fp.read()
            fp.close() 
        except:
            exit(errno.ENOENT)
                    
        m=re.search(r'(?:\.end|\.END)\s+', txt )
        new_txt = txt
        if m is not None:
            (start, end) = m.span()
            txt = txt[0:start]
        
        txt+=cmd + '\n'
        txt+='.END \n'
        try:
            fp= open(self.netlist+'.net', "w")
            fp.write(txt)
            fp.close() 
        except:
            exit(errno.ENOENT)
            
            
    def delString(self, cmd):
        '''
        Odstranenie povelu z netlistu bez doplnenia parametrov.
        
        Vyhlada a odstrani retazec podla zadaneho vzoru.
        '''
        try:
            fp= open(self.netlist+'.net', "r")
            txt = fp.read()
            fp.close() 
        except:
            exit(errno.ENOENT)
        
        m=re.search(cmd, txt )
        if m is not None:
            (start, end) = m.span()
            txt = txt[0:start]+txt[end+1:]
            
        try:
            fp= open(self.netlist+'.net', "w")
            fp.write(txt)
            fp.close() 
        except:
            exit(errno.ENOENT)
        
        

        
        
        
        
    

