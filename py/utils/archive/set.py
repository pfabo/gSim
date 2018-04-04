#!/usr/bin/env python
'''
Pomocna trieda pre modifikaciu/nastavenie parametrov simulacie.
'''


import os, sys, re


class gsimSet(): 
    
    def __init__(self,filename):
        self.filename=filename
    
    def openFile(self):
        
        # Otvorenie povodneho *.net suboru, nacitanie a otvorenie 
        # vystupneho suboru s rovnakym menom 
        try:
            inputFile = open(self.filename+'.net', "r")
            self.lines = inputFile.readlines()
            inputFile.close() 
        
            self.outputFile=open(self.filename+'.net',"w+")
            return True
        except:
            print ('Error open/write netlist file ' + self.filename+'.net')
            return False

    def findAndReplace(self, strFind, strReplace):
        
        if self.openFile() is False: 
            return
        
        # Prehladanie suboru po riadkoch, hladanie prikazu .PARAMS
        parFound=False
        
        for s in self.lines:
            q=''
            # prepisanie stareho parametra
            if re.match(strFind, s) is not None:
                q='-'
                self.outputFile.write(strReplace)
                parFound=True
                
            if re.match(r'.END', s.upper()) is not None:
                q='-'
                # doplnenie parametra, ak neexistuje/nebol najdeny
                if parFound is False:
                    self.outputFile.write(strReplace)
                self.outputFile.write('.END')
                
            # zapis do suboru
            if q=='':   
                self.outputFile.write(s)        # riadok bez zmeny
            else:
                pass

        self.outputFile.close()
        return  

