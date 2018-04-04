#!/usr/bin/env python
'''
Konverzia standardneho netlistu analogovych komponentov na rozsireny 
format XSPICE.  
'''
import os, fileinput, string, sys, re

def XSPICE_Analog(q,cmpData, attrList):
    
    # 5 - vstupny sumacny blok
    if re.match(r'SUMMER_5', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' ['+q[1]+' ' +q[2]+' '+q[3]+' '+q[4]+' '+q[5]+'] '+q[6]+' ' +q[7]+'_'+q[0]+'\n'+\
            '.MODEL '+q[7]+'_'+q[0]+' SUMMER (\n'                     +\
            '   + in_offset=[ ' + attrList.get('in_offset_1')+' '     +\
                                  attrList.get('in_offset_2')+' '     +\
                                  attrList.get('in_offset_3')+' '     +\
                                  attrList.get('in_offset_4')+' '     +\
                                  attrList.get('in_offset_5')+'] \n'  +\
            '   + in_gain=[ '   + attrList.get('in_gain_1')+' '       +\
                                  attrList.get('in_gain_2')+' '       +\
                                  attrList.get('in_gain_3')+' '       +\
                                  attrList.get('in_gain_4')+' '       +\
                                  attrList.get('in_gain_5')+'] \n'    +\
            '   + out_gain='    + attrList.get('out_gain')+'\n'       +\
            '   + out_offset='  + attrList.get('out_offset')+')'
        return str
    
    # 8 - vstupny sumacny blok
    if re.match(r'SUMMER_8', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' ['+q[1]+' ' +q[2]+' '+q[3]+' '+q[4]+' '+q[5]+' '+q[6]+' '+q[7]+' '+q[8]+'] ' +q[9]+' '+q[10]+'_'+q[0]+'\n'+\
            '.MODEL '+q[10]+'_'+q[0]+' SUMMER (\n'                    +\
            '   + in_offset=[ ' + attrList.get('in_offset_1')+' '     +\
                                  attrList.get('in_offset_2')+' '     +\
                                  attrList.get('in_offset_3')+' '     +\
                                  attrList.get('in_offset_4')+' '     +\
                                  attrList.get('in_offset_5')+' '     +\
                                  attrList.get('in_offset_6')+' '     +\
                                  attrList.get('in_offset_7')+' '     +\
                                  attrList.get('in_offset_8')+'] \n'  +\
            '   + in_gain=[ '   + attrList.get('in_gain_1')+' '       +\
                                  attrList.get('in_gain_2')+' '       +\
                                  attrList.get('in_gain_3')+' '       +\
                                  attrList.get('in_gain_4')+' '       +\
                                  attrList.get('in_gain_5')+' '       +\
                                  attrList.get('in_gain_6')+' '       +\
                                  attrList.get('in_gain_7')+' '       +\
                                  attrList.get('in_gain_8')+'] \n'    +\
            '   + out_gain='    + attrList.get('out_gain')+'\n'       +\
            '   + out_offset='  + attrList.get('out_offset')+')'
        return str
    
    # Jednoduchy zosilnovac
    if re.match(r'GAIN', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' '+q[1]+' ' +q[2]+' ' +q[3]+'_'+q[0]+'\n'         +\
            '.MODEL '+q[3]+'_'+q[0]+' GAIN (\n'                     +\
            '   + in_offset='   + attrList.get('in_offset')+'\n'    +\
            '   + out_offset='  + attrList.get('out_offset')+'\n'   +\
            '   + gain='        + attrList.get('gain')+' )'
        return str
    
    # 2 - vstupny sumacny blok
    if re.match(r'SUMMER_2', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' ['+q[1]+' ' +q[2]+'] '+q[3]+' ' +q[4]+'_'+q[0]+'\n'+\
            '.MODEL '+q[4]+'_'+q[0]+' SUMMER (\n'                     +\
            '   + in_offset=[ ' + attrList.get('in_offset_1')+' '     +\
                                  attrList.get('in_offset_2')+'] \n'  +\
            '   + in_gain=[ '   + attrList.get('in_gain_1')+' '       +\
                                  attrList.get('in_gain_2')+'] \n'    +\
            '   + out_gain='    + attrList.get('out_gain')+'\n'       +\
            '   + out_offset='  + attrList.get('out_offset')+')'
        return str
    
    # 2A - vstupovy diffrencialny blok
    #      vizualna uprava sumacneho bloku
    if re.match(r'DIFF_2', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' ['+q[1]+' ' +q[2]+'] '+q[3]+' ' +q[4]+'_'+q[0]+'\n'+\
            '.MODEL '+q[4]+'_'+q[0]+' SUMMER (\n'                     +\
            '   + in_offset=[ ' + attrList.get('in_offset_1')+' '     +\
                                  attrList.get('in_offset_2')+'] \n'  +\
            '   + in_gain=[ '   + attrList.get('in_gain_1')+' '       +\
                                  attrList.get('in_gain_2')+'] \n'    +\
            '   + out_gain='    + attrList.get('out_gain')+'\n'       +\
            '   + out_offset='  + attrList.get('out_offset')+')'

        return str
        
    # 3 - vstupny sumacny blok
    if re.match(r'SUMMER_3', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' ['+q[1]+' ' +q[2]+' '+q[3]+'] '+q[4]+' ' +q[5]+'_'+q[0]+'\n'+\
            '.MODEL '+q[5]+'_'+q[0]+' SUMMER (\n'                     +\
            '   + in_offset=[ ' + attrList.get('in_offset_1')+' '     +\
                                  attrList.get('in_offset_2')+' '     +\
                                  attrList.get('in_offset_3')+'] \n'  +\
            '   + in_gain=[ '   + attrList.get('in_gain_1')+' '       +\
                                  attrList.get('in_gain_2')+' '       +\
                                  attrList.get('in_gain_3')+'] \n'    +\
            '   + out_gain='    + attrList.get('out_gain')+'\n'       +\
            '   + out_offset='  + attrList.get('out_offset')+')'
        return str
        
    # 4 - vstupny sumacny blok
    if re.match(r'SUMMER_4', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' ['+q[1]+' ' +q[2]+' '+q[3]+' '+q[4]+'] '+q[5]+' ' +q[6]+'_'+q[0]+'\n'+\
            '.MODEL '+q[6]+'_'+q[0]+' SUMMER (\n'                     +\
            '   + in_offset=[ ' + attrList.get('in_offset_1')+' '     +\
                                  attrList.get('in_offset_2')+' '     +\
                                  attrList.get('in_offset_3')+' '     +\
                                  attrList.get('in_offset_4')+'] \n'  +\
            '   + in_gain=[ '   + attrList.get('in_gain_1')+' '       +\
                                  attrList.get('in_gain_2')+' '       +\
                                  attrList.get('in_gain_3')+' '       +\
                                  attrList.get('in_gain_4')+'] \n'    +\
            '   + out_gain='    + attrList.get('out_gain')+'\n'       +\
            '   + out_offset='  + attrList.get('out_offset')+')'
        return str
    
    # 2 - vstupny multiplikativny blok
    if re.match(r'MULT_2', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' ['+q[1]+' ' +q[2]+'] '+q[3]+' ' +q[4]+'_'+q[0]+'\n'+\
            '.MODEL '+q[4]+'_'+q[0]+' MULT (\n'                   +\
            '   + in_offset=[ ' + attrList.get('in_offset_1')+' '     +\
                                  attrList.get('in_offset_2')+'] \n'  +\
            '   + in_gain=[ '   + attrList.get('in_gain_1')+' '       +\
                                  attrList.get('in_gain_2')+'] \n'    +\
            '   + out_gain='    + attrList.get('out_gain')+'\n'       +\
            '   + out_offset='  + attrList.get('out_offset')+')'
        return str
    
    # 3 - vstupny multiplikativny blok
    if re.match(r'MULT_3', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' ['+q[1]+' ' +q[2]+' '+q[3]+'] '+q[4]+' ' +q[5]+'_'+q[0]+'\n'+\
            '.MODEL '+q[5]+'_'+q[0]+' MULT (\n'                   +\
            '   + in_offset=[ ' + attrList.get('in_offset_1')+' '     +\
                                  attrList.get('in_offset_3')+' '     +\
                                  attrList.get('in_offset_2')+'] \n'  +\
            '   + in_gain=[ '   + attrList.get('in_gain_1')+' '       +\
                                  attrList.get('in_gain_2')+' '       +\
                                  attrList.get('in_gain_3')+'] \n'    +\
            '   + out_gain='    + attrList.get('out_gain')+'\n'       +\
            '   + out_offset='  + attrList.get('out_offset')+')'
        return str
        
    # 4 - vstupny multiplikativny blok
    if re.match(r'MULT_4', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' ['+q[1]+' ' +q[2]+' '+q[3]+' '+q[4]+'] '+q[5]+' ' +q[6]+'_'+q[0]+'\n'+\
            '.MODEL '+q[6]+'_'+q[0]+' MULT (\n'                   +\
            '   + in_offset=[ ' + attrList.get('in_offset_1')+' '     +\
                                  attrList.get('in_offset_2')+' '     +\
                                  attrList.get('in_offset_3')+' '     +\
                                  attrList.get('in_offset_4')+'] \n'  +\
            '   + in_gain=[ '   + attrList.get('in_gain_1')+' '       +\
                                  attrList.get('in_gain_2')+' '       +\
                                  attrList.get('in_gain_3')+' '       +\
                                  attrList.get('in_gain_4')+'] \n'    +\
            '   + out_gain='    + attrList.get('out_gain')+'\n'       +\
            '   + out_offset='  + attrList.get('out_offset')+')'
        return str
        
    # 5 - vstupny sumacny blok
    if re.match(r'MULT_5', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' ['+q[1]+' ' +q[2]+' '+q[3]+' '+q[4]+' '+q[5]+'] '+q[6]+' ' +q[7]+'_'+q[0]+'\n'+\
            '.MODEL '+q[7]+'_'+q[0]+' MULT (\n'                   +\
            '   + in_offset=[ ' + attrList.get('in_offset_1')+' '     +\
                                  attrList.get('in_offset_2')+' '     +\
                                  attrList.get('in_offset_3')+' '     +\
                                  attrList.get('in_offset_4')+' '     +\
                                  attrList.get('in_offset_5')+'] \n'  +\
            '   + in_gain=[ '   + attrList.get('in_gain_1')+' '       +\
                                  attrList.get('in_gain_2')+' '       +\
                                  attrList.get('in_gain_3')+' '       +\
                                  attrList.get('in_gain_4')+' '       +\
                                  attrList.get('in_gain_5')+'] \n'    +\
            '   + out_gain='    + attrList.get('out_gain')+'\n'       +\
            '   + out_offset='  + attrList.get('out_offset')+')'
        return str
    
    # 8 - vstupny sumacny blok
    if re.match(r'MULT_8', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' ['+q[1]+' ' +q[2]+' '+q[3]+' '+q[4]+' '+q[5]+' '+q[6]+' '+q[7]+' '+q[8]+'] ' +q[9]+' '+q[10]+'_'+q[0]+'\n'+\
            '.MODEL '+q[10]+'_'+q[0]+' MULT (\n'                      +\
            '   + in_offset=[ ' + attrList.get('in_offset_1')+' '     +\
                                  attrList.get('in_offset_2')+' '     +\
                                  attrList.get('in_offset_3')+' '     +\
                                  attrList.get('in_offset_4')+' '     +\
                                  attrList.get('in_offset_5')+' '     +\
                                  attrList.get('in_offset_6')+' '     +\
                                  attrList.get('in_offset_7')+' '     +\
                                  attrList.get('in_offset_8')+'] \n'  +\
            '   + in_gain=[ '   + attrList.get('in_gain_1')+' '       +\
                                  attrList.get('in_gain_2')+' '       +\
                                  attrList.get('in_gain_3')+' '       +\
                                  attrList.get('in_gain_4')+' '       +\
                                  attrList.get('in_gain_5')+' '       +\
                                  attrList.get('in_gain_6')+' '       +\
                                  attrList.get('in_gain_7')+' '       +\
                                  attrList.get('in_gain_8')+'] \n'    +\
            '   + out_gain='    + attrList.get('out_gain')+'\n'       +\
            '   + out_offset='  + attrList.get('out_offset')+')'
        return str
    
    # Komparator s hysterezou
    if re.match(r'HYST', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        rtStr=        q[0]+' '+q[1]+' ' +q[2]+' ' +q[3]+'_'+q[0]+'\n'
        rtStr=rtStr + '.MODEL '+q[3]+'_'+q[0]+' HYST (\n'
        rtStr=rtStr + '   + in_low='          + attrList.get('in_low')+'\n'
        rtStr=rtStr + '   + in_high='         + attrList.get('in_high')+'\n'
        rtStr=rtStr + '   + hyst='            + attrList.get('hyst')+'\n'
        rtStr=rtStr + '   + out_lower_limit=' + attrList.get('out_lower_limit')+'\n'
        rtStr=rtStr + '   + out_upper_limit=' + attrList.get('out_upper_limit')+'\n'
        rtStr=rtStr + '   + input_domain='    + attrList.get('input_domain')+'\n'
        rtStr=rtStr + '   + fraction='        + attrList.get('fraction')+' )'
        return rtStr
        
    # Limiter (obmedzovac)
    if re.match(r'LIMIT', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        rtStr=        q[0]+' '+q[1]+' ' +q[2]+' ' +q[3]+'_'+q[0]+'\n'
        rtStr=rtStr + '.MODEL '+q[3]+'_'+q[0]+' LIMIT (\n'
        rtStr=rtStr + '   + in_offset='       + attrList.get('in_offset')+'\n'
        rtStr=rtStr + '   + gain='            + attrList.get('gain')+'\n'
        rtStr=rtStr + '   + out_lower_limit=' + attrList.get('out_lower_limit')+'\n'
        rtStr=rtStr + '   + out_upper_limit=' + attrList.get('out_upper_limit')+'\n'
        rtStr=rtStr + '   + limit_range='     + attrList.get('limit_range')+'\n'
        rtStr=rtStr + '   + fraction='        + attrList.get('fraction')+' )'
        return rtStr
        
    # Riadeny limiter (obmedzovac)
    if re.match(r'CLIMIT', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        rtStr=        q[0]+' '+q[1]+' ' +q[2]+' '+q[3]+' '+q[4]+' ' +q[5]+'_'+q[0]+'\n'
        rtStr=rtStr + '.MODEL '+q[5]+'_'+q[0]+' CLIMIT (\n'
        rtStr=rtStr + '   + in_offset='       + attrList.get('in_offset')+'\n'
        rtStr=rtStr + '   + gain='            + attrList.get('gain')+'\n'
        rtStr=rtStr + '   + upper_delta='     + attrList.get('upper_delta')+'\n'
        rtStr=rtStr + '   + lower_delta='     + attrList.get('lower_delta')+'\n'
        rtStr=rtStr + '   + limit_range='     + attrList.get('limit_range')+'\n'
        rtStr=rtStr + '   + fraction='        + attrList.get('fraction')+' )'
        return rtStr
        
    # Derivacny blok - differentiator 
    if re.match(r'D_DT', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        rtStr=        q[0]+' '+q[1]+' ' +q[2]+' ' +q[3]+'_'+q[0]+'\n'
        rtStr=rtStr + '.MODEL '+q[3]+'_'+q[0]+' D_DT (\n'
        rtStr=rtStr + '   + out_offset='       + attrList.get('out_offset')+'\n'
        rtStr=rtStr + '   + gain='            + attrList.get('gain')+'\n'
        rtStr=rtStr + '   + out_lower_limit=' + attrList.get('out_lower_limit')+'\n'
        rtStr=rtStr + '   + out_upper_limit=' + attrList.get('out_upper_limit')+'\n'
        rtStr=rtStr + '   + limit_range='     + attrList.get('limit_range')+' )'
        return rtStr
    
    # Integrator
    if re.match(r'INT', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        rtStr=        q[0]+' '+q[1]+' ' +q[2]+' ' +q[3]+'_'+q[0]+'\n'
        rtStr=rtStr + '.MODEL '+q[3]+'_'+q[0]+' INT (\n'
        rtStr=rtStr + '   + in_offset='       + attrList.get('in_offset')+'\n'
        rtStr=rtStr + '   + gain='            + attrList.get('gain')+'\n'
        rtStr=rtStr + '   + out_lower_limit=' + attrList.get('out_lower_limit')+'\n'
        rtStr=rtStr + '   + out_upper_limit=' + attrList.get('out_upper_limit')+'\n'
        rtStr=rtStr + '   + limit_range='     + attrList.get('limit_range')+' \n'
        rtStr=rtStr + '   + out_ic='     + attrList.get('out_ic')+' )'
        return rtStr
    
    # Analog switch
    if re.match(r'ASWITCH', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        rtStr=        q[0]+' '+q[1]+' (' +q[2]+' ' +q[3]+') '+q[4]+'_'+q[0]+'\n'
        rtStr=rtStr + '.MODEL '+q[4]+'_'+q[0]+' ASWITCH (\n'
        rtStr=rtStr + '   + cntl_off=' + attrList.get('cntl_off')+'\n'
        rtStr=rtStr + '   + cntl_on='  + attrList.get('cntl_on')+'\n'
        rtStr=rtStr + '   + r_off='    + attrList.get('r_off')+'\n'
        rtStr=rtStr + '   + r_on='     + attrList.get('r_on')+'\n'
        rtStr=rtStr + '   + log='      + attrList.get('log')+' )'
        return rtStr
        
    # S-Domain Transfer Function
    if re.match(r'S_XFER', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        str=q[0]+' '+q[1]+' ' +q[2]+' ' +q[3]+'_'+q[0]+'\n'         +\
            '.MODEL '+q[3]+'_'+q[0]+' S_XFER (\n'                   +\
            '   + in_offset='   + attrList.get('in_offset')+'\n'    +\
            '   + int_ic='      +attrList.get('int_ic')+'\n'   +\
            '   + denormalized_freq=' + attrList.get('denormalized_freq')+'\n'  +\
            '   + num_coeff='   + attrList.get('num_coeff')+'\n'    +\
            '   + den_coeff='   + attrList.get('den_coeff')+'\n'    +\
            '   + gain='        + attrList.get('gain')+' )'
        return str
    return ''

