#!/usr/bin/env python
'''
Jednoduchy pre/post procesor pre gschem & ngspice & xyce

- kontrola zapojenia (duplicitne a nedefinovane referencie)
- vyhladanie a doplnenie ciest k modelom komponentov
- uprava atributov pre xspice (ngspice) a ABM (xyce) bloky
- nastavenie zakladnych typov analyz doplnenim do nelistu (.DC, .AC, .TRAN)
- moznost doplnenia a mazania prikazov z netlistu pre opakovane analyzy
  bez potreby editovania zapojenia alebo netlistu
'''
import os, sys, errno
from scipy import *
from net.convert import ConvertNetlist
from utils import *
from config import * 


class gSim():

    def __init__(self, filename, engine='NGSPICE'):
        '''
        Inicializacia vstupnych parametrov simulacie a kontrola existencie
        suboru so zapojenim.
        
        Parametre:
        filename - meno suboru so zapojenim z gschem (*.sch)
        engine   - typ simulatora, 'NGSPICE', 'XYCE'
        
        '''
        self.filename = ''      # simulator input filename
        self.c_list = []        # zoznam komponentov schemy
        self.m_list = {}        # slovnik pouzitych modelov typ <-> model  
        
        # existencia vstupneho suboru so zapojenim
        if not os.path.exists(filename):
            print('Error: File ' + filename + 'not present')
            exit(errno.ENOENT)
            
        # meno projektu odvodene z mena suboru zapojenia
        self.filename = filename.split('.sch')[0]
        
        # vytvorenie adresara pre medzivysledky
        if os.path.isdir(config.PATH_TEMP) is False:
            os.mkdir(config.PATH_TEMP)
            
        self.writeLog = False   # vystup z konzoly do suboru 
        
        self.engine=engine      # typ simulacneho engine
                                # NGSPICE
                                # XYCE
                                
        # Parser suboru *.sch - vytvorenie zoznam komponentov v zapojeni
        pr = parser.gschParser(self.filename + ".sch")
        self.c_list = pr.component()
        
        self.cnv = ConvertNetlist(config.PATH_TEMP + self.filename, self.c_list)

    def netlist(self):
        '''
        Vytvorenie a modifikacia netlistu zo zapojenia obvodu zadanom
        v konstruktore triedy.
        
        Postup:
        - kontrola na nedefinovane a/alebo duplicitne referencie
        - vytvorenie netlistu pomocou standardneho programu gnetlist
        - vytvorenie kopie originalneho netlistu 
        - modifikacia netlistu, doplnenie modelov komponentov,
          doplnenie parametrov pre xspice a xyce 
        '''
        logOutput = ''
        if self.writeLog is True:
            logOutput = " > " + config.PATH_TEMP + 'log-netlist.txt'
        
        # Kontrola duplicitnych a nedefinovanych referencii v scheme
        # pomocou atributu refdes
        refList = {}
        err = False
        for i in self.c_list:           # nacitanie referencii komponentov V1, R3 ...
            ref = i.get('attributes', {}).get('refdes', {}).get('data', None)   
            
            if ref is not None:
                value = i.get('attributes', {}).get('value', {}).get('data', None)
                
                if ref.find('?') >= 0:  # kontrola na referenciu obsahujucu '?'
                    print('Error: nedefinovana referencia ' + ref + ',' + value)
                    err = True

                if ref in refList:      # kontrola duplicitnej referencie v ulozenom zozname
                    print ('Error: duplicitna refrerencia ', refList.get(ref), '=>', ref, ",", value)
                    err = True  
                else:
                    # zaradenie referencie do zoznamu
                    refList[ref] = ref
        if err:
            print ('Error: chyba v zapojeni ' + self.filename +'.sch, netlist nebol vytvoreny.')
            exit()

        # Vytvorenie netlistu
        cmd = "gnetlist -q -g spice-sdb " + self.filename + ".sch -o " + config.PATH_TEMP + self.filename + ".net" \
                                          + logOutput
        os.system(cmd)
        
        # Kopia povodneho netlistu -> do suboru .txt
        cmd = "cp " + config.PATH_TEMP + self.filename + ".net " + config.PATH_TEMP + self.filename + ".txt"
        os.system(cmd)

        # 5. Upravy netlistu, doplnenie modelov
        self.m_list = self.cnv.update()

    def sim(self, mode='RAW'):
        '''
        Spustenie simulacie pre zvoleny typ engine.  
        
        Parametre:
        mode - urcuje typ simulacie
              'RAW'  - vytvori a extrahuje data z raw suboru, ignoruje 
                       prikazy .PRINT v zapojeni obvodu, format *.raw
                       suboru zavisi od typu engine 
              'PRINT'- vytvori vystupy podla prikazu(-ov) v zapojeni,
                       vystup zavisi od typu engine
        '''
        if self.engine == 'NGSPICE':
            return self.__ng_sim(mode)
            
        elif self.engine == 'XYCE':
            return self.__xc_sim(mode)
            
        print('Error: Unknown simulation engine type ' + self.engineType)
        return (None,None)
            
    def __ng_sim(self, mode='RAW'):
        '''
        Spusti simulaciu v ngspice podla prepinaca
        'RAW'     - vytvori a extrahuje data z raw suboru, ignoruje prikazy .PRINT v *.sch
        'PRINT'   - vytvori vystupy podla prikazov v zapojeni
        '''
        logOutput = ''
        if self.writeLog is True:
            logOutput = '> ./tmp/log-ngspice.txt'
        
        if mode == 'RAW':
            cmd = 'rm -f ./tmp/*.raw '
            os.system(cmd)
            
            cmd = "ngspice -b -a " + config.PATH_TEMP + self.filename + ".net -r " \
                                   + config.PATH_TEMP + self.filename + ".raw "    \
                                   + logOutput
            os.system(cmd)

            if not os.path.isfile(config.PATH_TEMP + self.filename + ".raw"):
                print ("Error: v simulacii nebol subor " + config.PATH_TEMP + self.filename + ".raw vytvoreny")
                exit()
            
            data, desc = raw.read(config.PATH_TEMP + self.filename + ".raw")
            return (data, desc)
        
        else:
            cmd = "ngspice -b -a " + config.PATH_TEMP + self.filename + ".net " \
                                   + logOutput
            os.system(cmd)
            return (None, None)
            
    def __xc_sim(self, mode='RAW'):
        '''
        Spusti simulaciu v Xyce podla prepinaca
        'RAW'     - vytvori a extrahuje data z raw suboru, ignoruje prikazy .PRINT v *.sch
        'PRINT'   - vytvori vystupy podla prikazov v zapojeni
        '''
        logOutput = ''
        if self.writeLog is True:
            logOutput = ' -l ./tmp/log-xyce.txt'
        
        if mode == 'RAW':
            cmd = 'rm -f ./tmp/*.raw '
            os.system(cmd)
            
            cmd = 'Xyce ' + config.PATH_TEMP + self.filename + '.net -r '     \
                          + config.PATH_TEMP + self.filename + '.raw ' \
                          + logOutput
            os.system(cmd)
            
            if not os.path.isfile(config.PATH_TEMP + self.filename + ".raw"):
                print ("Error: v simulacii nebol subor " + config.PATH_TEMP + self.filename + ".raw vytvoreny")
                exit()
            
            data, desc = raw.read(config.PATH_TEMP + self.filename + ".raw")
            return (data, desc)
            
        else:
            cmd = "Xyce " + config.PATH_TEMP + self.filename + ".net -quiet" \
                          + logOutput
            os.system(cmd)
            return (None, None)
            
    def setAC(self, start, stop, number=100, typ='LIN'):
        '''
        Nastavenie .AC analyzy (frekvencna charakteristika)
        
        Vyhlada a odstrani predchadzajuci .AC prikaz (ak existoval) 
        a nahradi ho novym prikazom.
        
        Parametre:
        start  - pociatok frekvencneho rozsahu
        stop   - koniec frekvencneho rozsahu
        number - pocet bodov charakteristiky
        typ    - delenie frekvencneho rozsahu 'LIN', 'OCT', 'DEC'
        '''
        ac = r'.AC ' + typ + ' ' + str(number) + ' ' + str(start) + ' ' + str(stop) 
        
        #cmd='.AC'
        #cstr = r'(?:'+('\\'+cmd).upper() + ('|\\'+cmd).lower()+')'
        #self.cnv.delCommand(cstr)
        self.cnv.delString(r'(?:\.AC|\.ac)\s+([a-zA-Z0-9 \.\(\)])+')
        self.cnv.addString(ac)

    def setTRAN(self, step, stop, start=0.0, tmax=0.0, uic=False):
        '''
        Nastavenie .TRAN analyzy (casova odozva)
        
        Vyhlada a odstrani predchadzajuci .TRAN prikaz (ak existoval) 
        a nahradi ho novym prikazom.
        
        Parametre:
        step  - casovy krok
        stop  - koniec casoveho intervalu
        start - posunutie zaciatku casu analyzy (ustalenie obvodu)
        uic   - ak je True, doplni argument 'UIC' do prikazu
        '''
        tran = r'.TRAN ' + str(step) + ' ' + str(stop) + ' ' + str(start) + ' '
        if tmax > 0.0:
            tran += str(tmax) + ' '
        if uic is True:
            tran += 'UIC' 
                
        #cmd='.TRAN'
        #cstr = r'(?:'+('\\'+cmd).upper() + ('|\\'+cmd).lower()+')'
        #self.cnv.delCommand(cstr)
        self.cnv.delString(r'(?:\.TRAN|\.tran)\s+([a-zA-Z0-9 \.\(\)])+')
        self.cnv.addString(tran)
        
    def setDC(self, src, start, stop, incr, typ='LIN' ):
        '''
        Nastavenie .DC analyzy (parametricka a jednosmerna analyza)
        
        Parametre:
        src   - meno komponentu, ktoreho hodnota sa bude menit napr. 'V1', 'R1'
        start - pociatocna hodnota parametru
        stop  - konecna hodnota parametru
        incr  - krok parametru
        typ   - typ delenia rozsahu (len pre XYCE), 'LIN', 'LOG','OCT'
        '''
        dc = r'.DC '
        if self.engine == 'NGSPICE':
            dc = dc + src +' ' + str(start) +' ' + str(stop) + ' ' + str(incr)
                
        elif self.engine == 'XYCE':
            dc = dc + typ +' '+ src +' ' + str(start) +' ' + str(stop) + ' ' + str(incr)
        
        #cmd='.DC'
        #cstr = r'(?:'+('\\'+cmd).upper() + ('|\\'+cmd).lower()+')'
        #self.cnv.delCommand(cstr)
        self.cnv.delString(r'(?:\.DC|\.dc)\s+([a-zA-Z0-9 \.\(\)])+')
        self.cnv.addString(dc)
        

    def setPAR(self, parName, parValue):
        '''
        Doplni prikazy .PARAMS do netlistu, predchadzajuce prikazy .PARAMS
        s rovnakym menom parName prepise. 
        Pre kazdy parameter generuje samostatny prikaz .PARAMS.
        '''
        par = r'.PARAM ' + parName + '=' + str(parValue)
        
        cstr = r'.PARAM\s+' + parName +r'=([a-zA-Z0-9\-\.= ])+'
        self.cnv.delString(cstr)
        self.cnv.addString(par)
        
    def addCMD(self, strCmd):
        '''
        Doplni vseobecny povelovy retazec do netlistu
        '''
        self.cnv.addString(strCmd)
        
    def delCMD(self, cmd):
        '''
        Odstranenie riadku so zadanym prikazom z netlistu
        
        Odstrani prikaz spolu s argumentami az po znak novehom riadku.
        '''
        cstr = r'(?:'+('\\'+cmd).upper() + ('|\\'+cmd).lower()+')'
        self.cnv.delString(r''+cstr+'\s+([a-zA-Z0-9 \'\-\.\(\)])+')
        
    def delCOMP(self, name):
        '''
        Odstranenie riadku so zadanym menom komponentu z netlistu
        '''
        cstr = r'(?:'+name.upper() + '|' +name.lower()+')'
        self.cnv.delString(r''+cstr+'\s+([a-zA-Z0-9 \'\-\.\(\)])+')
        
        
def gs(filename, engine='NGSPICE', typ='RAW'):
    '''
    Funkcia pre zjednodusene spustenie analyzy v programe.
    
    Nacita suboru, vygeneruje netlistu a spusti simulacie.
    '''
    q = gSim(filename, engine)
    q.netlist()
    return q.sim(typ)

if __name__ == '__main__':
    '''
    Spustenie simulacie z poveloveho riadku.
    
    Kontrola argumentov poveloveho riadku a spustenie simulacie
    '''
    if len(sys.argv) < 2 :
        print ("Use: python3 gsim.py filename.sch [-engine], [-type]")
        print ("     -engine = -NGSPICE, -XYCE  simulation engine ")
        print ("     -type   = -RAW, -PRINT     simulation output type ")
        exit()
    
    engine = 'NGSPICE'
    typ = 'RAW'
    for s in sys.argv:
        if s.upper()=='-XYCE':
            engine='XYCE'
        if s.upper()=='-PRINT':
            typ ='PRINT'
       
    # kontrola existencie mena suboru *.sch
    if not os.path.isfile(sys.argv[1]):
        print ("Error open file ", sys.argv[1])
        exit()
    
    q = gSim(sys.argv[1],engine)
    q.netlist()
    q.sim(typ)
    
