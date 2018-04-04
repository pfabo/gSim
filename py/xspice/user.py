#!/usr/bin/env python
'''
Konverzia uzivatelom definovanych komponentov XSPICE
'''
import os, fileinput, string, sys, re

def XSPICE_User(q,cmpData, attrList):

    if re.match(r'D_LEVEL_H', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov         
        str= q[0]+' '+q[1]+' '+q[2]+'_'+q[0]+'\n' +\
             '.MODEL '+q[2]+'_'+q[0]+' D_LEVEL_H (\n)'
        return str
            
    if re.match(r'D_LEVEL_L', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov         
        str= q[0]+' '+q[1]+' '+q[2]+'_'+q[0]+'\n' +\
             '.MODEL '+q[2]+'_'+q[0]+' D_LEVEL_L ' # (\n)'
        return str
        
    # Matematicka funkcia y=x^2
    if re.match(r'M_SQUARE', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' '+q[1]+' ' +q[2]+' ' +q[3]+'_'+q[0]+'\n'         +\
            '.MODEL '+q[3]+'_'+q[0]+' M_SQUARE (\n'                     +\
            '   + in_offset='   + attrList.get('in_offset')+'\n'    +\
            '   + out_offset='  + attrList.get('out_offset')+'\n'   +\
            '   + gain='        + attrList.get('gain')+' )'
        return str
        
    # Matematicka funkcia y=sqrt(x)
    if re.match(r'M_SQRT', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' '+q[1]+' ' +q[2]+' ' +q[3]+'_'+q[0]+'\n'         +\
            '.MODEL '+q[3]+'_'+q[0]+' M_SQRT (\n'                       +\
            '   + in_offset='   + attrList.get('in_offset')+'\n'    +\
            '   + out_offset='  + attrList.get('out_offset')+'\n'   +\
            '   + gain='        + attrList.get('gain')+' )'
        return str
        
    # Matematicka funkcia y=sin(x)
    if re.match(r'M_SIN', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' '+q[1]+' ' +q[2]+' ' +q[3]+'_'+q[0]+'\n'         +\
            '.MODEL '+q[3]+'_'+q[0]+' M_SIN (\n'                        +\
            '   + in_offset='   + attrList.get('in_offset')+'\n'    +\
            '   + out_offset='  + attrList.get('out_offset')+'\n'   +\
            '   + gain='        + attrList.get('gain')+' )'
        return str
        
    # Matematicka funkcia y=cos(x)
    if re.match(r'M_COS', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' '+q[1]+' ' +q[2]+' ' +q[3]+'_'+q[0]+'\n'         +\
            '.MODEL '+q[3]+'_'+q[0]+' M_COS (\n'                        +\
            '   + in_offset='   + attrList.get('in_offset')+'\n'    +\
            '   + out_offset='  + attrList.get('out_offset')+'\n'   +\
            '   + gain='        + attrList.get('gain')+' )'
        return str
    
    # Matematicka funkcia y=abs(x)
    if re.match(r'M_ABS', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' '+q[1]+' ' +q[2]+' ' +q[3]+'_'+q[0]+'\n'         +\
            '.MODEL '+q[3]+'_'+q[0]+' M_ABS (\n'                        +\
            '   + in_offset='   + attrList.get('in_offset')+'\n'    +\
            '   + out_offset='  + attrList.get('out_offset')+'\n'   +\
            '   + gain='        + attrList.get('gain')+' )'
        return str

    # Matematicka funkcia y=1/x
    if re.match(r'M_INV', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' '+q[1]+' ' +q[2]+' ' +q[3]+'_'+q[0]+'\n'         +\
            '.MODEL '+q[3]+'_'+q[0]+' M_INV (\n'                        +\
            '   + in_offset='   + attrList.get('in_offset')+'\n'    +\
            '   + out_offset='  + attrList.get('out_offset')+'\n'   +\
            '   + gain='        + attrList.get('gain')+' )'
        return str
        
    # Matematicka funkcia y=acos(x)
    if re.match(r'M_ACOS', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' '+q[1]+' ' +q[2]+' ' +q[3]+'_'+q[0]+'\n'         +\
            '.MODEL '+q[3]+'_'+q[0]+' M_ACOS (\n'                       +\
            '   + in_offset='   + attrList.get('in_offset')+'\n'    +\
            '   + out_offset='  + attrList.get('out_offset')+'\n'   +\
            '   + gain='        + attrList.get('gain')+' )'
        return str
        
    # Matematicka funkcia y=asin(x)
    if re.match(r'M_ASIN', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' '+q[1]+' ' +q[2]+' ' +q[3]+'_'+q[0]+'\n'         +\
            '.MODEL '+q[3]+'_'+q[0]+' M_ASIN (\n'                       +\
            '   + in_offset='   + attrList.get('in_offset')+'\n'    +\
            '   + out_offset='  + attrList.get('out_offset')+'\n'   +\
            '   + gain='        + attrList.get('gain')+' )'
        return str
        
    # Matematicka funkcia y=exp(x)
    if re.match(r'M_EXP', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' '+q[1]+' ' +q[2]+' ' +q[3]+'_'+q[0]+'\n'         +\
            '.MODEL '+q[3]+'_'+q[0]+' M_EXP (\n'                        +\
            '   + in_offset='   + attrList.get('in_offset')+'\n'    +\
            '   + out_offset='  + attrList.get('out_offset')+'\n'   +\
            '   + gain='        + attrList.get('gain')+' )'
        return str
        
    # Matematicka funkcia y=ln(x)
    if re.match(r'M_LN', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' '+q[1]+' ' +q[2]+' ' +q[3]+'_'+q[0]+'\n'         +\
            '.MODEL '+q[3]+'_'+q[0]+' M_LN (\n'                     +\
            '   + in_offset='   + attrList.get('in_offset')+'\n'    +\
            '   + out_offset='  + attrList.get('out_offset')+'\n'   +\
            '   + gain='        + attrList.get('gain')+' )'
        return str

    # Matematicka funkcia y=log(x)
    if re.match(r'M_LOG', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' '+q[1]+' ' +q[2]+' ' +q[3]+'_'+q[0]+'\n'         +\
            '.MODEL '+q[3]+'_'+q[0]+' M_LOG (\n'                    +\
            '   + in_offset='   + attrList.get('in_offset')+'\n'    +\
            '   + out_offset='  + attrList.get('out_offset')+'\n'   +\
            '   + gain='        + attrList.get('gain')+' )'
        return str
    
    # Zdroj analogovych dat zo suboru
    if re.match(r'A_SOURCE', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' '+q[1]+' ' +q[2]+'_'+q[0]+'\n'                       +\
            '.MODEL '+q[2]+'_'+q[0]+' A_SOURCE (\n'                     +\
            '   + input_file =\"'+ attrList.get('input_file' )+'\"\n'   +\
            '   + time_start ='  + attrList.get('time_start' )+'\n'     +\
            '   + time_delta ='  + attrList.get('time_delta' )+'\n'     +\
            '   + time_repeat='  + attrList.get('time_repeat')+'\n'     +\
            '   + channel    =\"'+ attrList.get('channel'    )+'\"\n'   +\
            '   + out_offset ='  + attrList.get('out_offset' )+'\n'     +\
            '   + out_gain   ='  + attrList.get('out_gain'   )+' )'
        return str
        
    return ''


