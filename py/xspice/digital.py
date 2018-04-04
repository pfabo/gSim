#!/usr/bin/env python
'''
Konverzia digitalnych komponentov XSPICE

'''
import os, fileinput, string, sys, re

def XSPICE_Digital(q,cmpData, attrList):
    
    # Blokovy model hradla, 1 vstup
    if (re.match(r'D_BUFFER', cmpData.attrValue('value').upper() )!=None) or\
       (re.match(r'D_INVERTER', cmpData.attrValue('value').upper() )!=None) :
        # Vytvorenie modelu z atributov         
        str= q[0]+' '+q[1]+' ' +q[2]+' '+q[3]+'_'+q[0]+'\n' +\
             '.MODEL '+q[3]+'_'+q[0]+' '+q[3]+' (\n'                          +\
             '   + rise_delay=' + attrList.get('rise_delay')+'\n'         +\
             '   + fall_delay=' + attrList.get('fall_delay')+'\n'         +\
             '   + input_load=' + attrList.get('input_load')+' )'
        return str
    
    # Blokovy model hradla, 2 vstupy
    if (re.match(r'D_NAND_2', cmpData.attrValue('value').upper() )!=None) or \
       (re.match(r'D_AND_2',  cmpData.attrValue('value').upper() )!=None) or \
       (re.match(r'D_OR_2',   cmpData.attrValue('value').upper() )!=None) or \
       (re.match(r'D_NOR_2',  cmpData.attrValue('value').upper() )!=None) or \
       (re.match(r'D_XOR_2',  cmpData.attrValue('value').upper() )!=None) or \
       (re.match(r'D_XNOR_2', cmpData.attrValue('value').upper() )!=None) :
        # Vytvorenie modelu z atributov         
        str= q[0]+' ['+q[1]+' ' +q[2]+'] ' + q[3]+ ' '+q[4]+'_'+q[0]+'\n' +\
             '.MODEL '+q[4]+'_'+q[0]+' '+q[4][0:-2]+' (\n'                    +\
             '   + rise_delay=' + attrList.get('rise_delay')+'\n'         +\
             '   + fall_delay=' + attrList.get('fall_delay')+'\n'         +\
             '   + input_load=' + attrList.get('input_load')+' )'
        return str
        
    # Blokovy model hradla, 3 vstupy
    if (re.match(r'D_NAND_3', cmpData.attrValue('value').upper() )!=None) or \
       (re.match(r'D_AND_3',  cmpData.attrValue('value').upper() )!=None) or \
       (re.match(r'D_OR_3',   cmpData.attrValue('value').upper() )!=None) or \
       (re.match(r'D_NOR_3',  cmpData.attrValue('value').upper() )!=None) :
        # Vytvorenie modelu z atributov         
        str= q[0]+' ['+q[1]+' ' +q[2]+' '+q[3]+'] ' + q[4]+ ' '+q[5]+'_'+q[0]+'\n' +\
             '.MODEL '+q[5]+'_'+q[0]+' '+q[5][0:-2]+' (\n'                    +\
             '   + rise_delay=' + attrList.get('rise_delay')+'\n'         +\
             '   + fall_delay=' + attrList.get('fall_delay')+'\n'         +\
             '   + input_load=' + attrList.get('input_load')+' )'
        return str
    
    # Blokovy model hradla, 4 vstupy
    if (re.match(r'D_NAND_4', cmpData.attrValue('value').upper() )!=None) or \
       (re.match(r'D_AND_4',  cmpData.attrValue('value').upper() )!=None) or \
       (re.match(r'D_OR_4',   cmpData.attrValue('value').upper() )!=None) or \
       (re.match(r'D_NOR_4',  cmpData.attrValue('value').upper() )!=None) :
        # Vytvorenie modelu z atributov         
        str= q[0]+' ['+q[1]+' ' +q[2]+' '+q[3]+' ' +q[4]+'] ' + q[5]+ ' '+q[6]+'_'+q[0]+'\n' +\
             '.MODEL '+q[6]+'_'+q[0]+' '+q[6][0:-2]+' (\n'                    +\
             '   + rise_delay=' + attrList.get('rise_delay')+'\n'         +\
             '   + fall_delay=' + attrList.get('fall_delay')+'\n'         +\
             '   + input_load=' + attrList.get('input_load')+' )'
        return str
    
    # Blokovy model NAND hradla, 8 vstupov
    if (re.match(r'D_NAND_8', cmpData.attrValue('value').upper() )!=None) or \
       (re.match(r'D_AND_8',  cmpData.attrValue('value').upper() )!=None) or \
       (re.match(r'D_OR_8',   cmpData.attrValue('value').upper() )!=None) or \
       (re.match(r'D_NOR_8',  cmpData.attrValue('value').upper() )!=None) :
        # Vytvorenie modelu z atributov         
        str= q[0]+' ['+q[1]+' ' +q[2]+' '+q[3]+' '+q[4]+' '+q[5]+' '+q[6]+' '+q[7]+' '+q[8]+'] ' + q[9]+ ' '+q[10]+'_'+q[0]+'\n' +\
             '.MODEL '+q[10]+'_'+q[0]+' '+q[10][0:-2]+' (\n'                      +\
             '   + rise_delay=' + attrList.get('rise_delay')+'\n'         +\
             '   + fall_delay=' + attrList.get('fall_delay')+'\n'         +\
             '   + input_load=' + attrList.get('input_load')+' )'
        return str
    
    # Blokovy model klopny obvod D, set a reset vstupy
    if re.match(r'D_DFF', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov         
        str= q[0]+' '+q[1]+' '+q[2]+' '+q[3]+' '+q[4]+' '+q[5]+' '+q[6]+' '+q[7]+'_'+q[0]+'\n' +\
             '.MODEL '+q[7]+'_'+q[0]+' D_DFF (\n'                       +\
             '   + rise_delay='  + attrList.get('rise_delay')+'\n'      +\
             '   + fall_delay='  + attrList.get('fall_delay')+'\n'      +\
             '   + set_load='    + attrList.get('set_load')  +'\n'      +\
             '   + reset_load='  + attrList.get('reset_load')+'\n'      +\
             '   + data_load='   + attrList.get('data_load')+'\n'       +\
             '   + clk_load='    + attrList.get('clk_load')+'\n'        +\
             '   + reset_delay=' + attrList.get('reset_delay')+'\n'     +\
             '   + ic='          + attrList.get('ic')+'\n'              +\
             '   + clk_delay='   + attrList.get('clk_delay')+'\n'       +\
             '   + set_delay='   + attrList.get('set_delay')+ ' )'
        return str
    return ''

