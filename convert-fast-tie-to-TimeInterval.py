# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 19:00:00 2015

@author: tom
"""

#Convert ramp voltages to time intervals
#Ramp tics are defined as precise time from system clock
#Many output samples.  Pick one each time the value changes


file = open("tie_vec_outfile")
file2 = open("TimeIntervals", 'w')

Vprev = float(file.readline())

numsamples = 0
dropped = 0

while file:
    instring = file.readline()
    if not instring:
        break

    Vnext = float(instring)

    Vdelta = Vnext - Vprev
    Vprev = Vnext

    if Vdelta == 0.0:   # throw out about 47 duplicate samples
        continue
    
    if Vdelta < 0.0:
        Vdelta += 1.0   # 10-second sawtooth ramp rolled over
        
    TI = Vdelta * 1000.0

    # deglitch the Time Interval problem in the Hermes SDR
    # throw out significant phase hits

    if TI > 102 or TI < 98:
        dropped += 1
    else:
        file2.write(str(TI)+'\n')  
       
    numsamples+=1
 
 
print "Processed samples = ",numsamples,"   Dropped outliers = ",dropped
 
file.close
file2.flush()
file2.close

 
