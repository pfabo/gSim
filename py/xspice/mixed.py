#!/usr/bin/env python
'''
Konverzia analogovo-digitalnych komponentov XSPICE
'''
import os, fileinput, string, sys, re

def XSPICE_Mixed(q,cmpData, attrList):
    # prevodnik signalov ANALOG/DIGITAL
    if re.match(r'ADC_BRIDGE', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        rtStr=        q[0]+' ['+q[1]+'] [' +q[2]+'] ' +q[3]+'_'+q[0]+'\n'
        rtStr=rtStr + '.MODEL '+q[3]+'_'+q[0]+' ADC_BRIDGE (\n'
        rtStr=rtStr + '   + in_low='     + attrList.get('in_low')+'\n'
        rtStr=rtStr + '   + in_high='    + attrList.get('in_high')+'\n'
        rtStr=rtStr + '   + rise_delay=' + attrList.get('rise_delay')+'\n'
        rtStr=rtStr + '   + fall_delay=' + attrList.get('fall_delay')+')'
        return rtStr
        
    # prevodnik signalov DIGITAL/ANALOG
    if re.match(r'DAC_BRIDGE', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        rtStr=        q[0]+' ['+q[1]+'] [' +q[2]+'] ' +q[3]+'_'+q[0]+'\n'
        rtStr=rtStr + '.MODEL '+q[3]+'_'+q[0]+' DAC_BRIDGE (\n'
        rtStr=rtStr + '   + out_low='    + attrList.get('out_low')+'\n'
        rtStr=rtStr + '   + out_high='   + attrList.get('out_high')+'\n'
        rtStr=rtStr + '   + out_undef='  + attrList.get('out_undef')+'\n'
        rtStr=rtStr + '   + t_rise='     + attrList.get('t_rise')+'\n'
        rtStr=rtStr + '   + t_fall='     + attrList.get('t_fall')+' )'
        return rtStr
        
    # Analogovym napetim riadeny digitalny oscilator
    if re.match(r'D_OSC', cmpData.attrValue('value').upper() )!=None:
        # Vytvorenie modelu z atributov
        rtStr=        q[0]+' '+q[1]+' ' +q[2]+' ' +q[3]+'_'+q[0]+'\n'
        rtStr=rtStr + '.MODEL '+q[3]+'_'+q[0]+' D_OSC (\n'
        rtStr=rtStr + '   + cntl_array=' + attrList.get('cntl_array')+'\n'
        rtStr=rtStr + '   + freq_array=' + attrList.get('freq_array')+'\n'
        rtStr=rtStr + '   + duty_cycle=' + attrList.get('duty_cycle')+'\n'
        rtStr=rtStr + '   + rise_delay=' + attrList.get('rise_delay')+'\n'
        rtStr=rtStr + '   + fall_delay=' + attrList.get('fall_delay')+' )'
        return rtStr
        
    return ''
