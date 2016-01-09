#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 2 10:00:00 2016

@author: Tom McDermott, N5EG
"""

#Convert integer ramp integers to time intervals, value
#is dependent on the sample rate. Output in nanoseconds.
#Many output samples - decimate to one each time the value
#changes. Accumulate time interval from each sample.

#Should work in Python 2.7 and 3


import sys
import struct

Vnext = 0
Vprev = 0
rawsamples = 0
numsamples = 0
dropped = 0
AccumTime = 0.0    #initially no accumulated error
samprate = 48000
outputsamples = 0

#samprate = int(input('Enter sample rate per second [e.g. 48000 or 384000]: '))

def emitTimeInterval(instring):

    global Vprev, Vnext, dropped, numsamples, AccumTime, samprate
    global outputsamples
    Vnext = int(instring)

    Vdelta = Vnext - Vprev
    Vprev = Vnext

    if Vdelta == 0:   # throw out (47 to 383) duplicate samples
        return
    
    if Vdelta < 0:
        Vdelta += (samprate * 10)   # 10-second sawtooth ramp rolled over
        
    TI = Vdelta * 100.0 / samprate

    # deglitch the Time Interval problem in the Hermes SDR
    # throw out significant phase hits

    if TI > 110.0 or TI < 90.0:
        dropped += 1
    else:
        AccumTime += (TI - 100.0)
        CorrectedTI = TI + AccumTime
        file2.write(str(CorrectedTI)+'\n')
        outputsamples += 1
       
    numsamples+=1



file = open("tie-vector", 'rb')
file2 = open("TimeIntervals", 'w')

while file:
    inbin = bytearray(file.read(4))
    if not inbin:
        break
    val = struct.unpack('i', inbin)[0]
    emitTimeInterval(str(val)+'\n')
    rawsamples+=1

file.close
file2.flush()
file2.close

vers = str(sys.version_info[0])+'.'+str(sys.version_info[1])+'.'+str(sys.version_info[2])

print ("Python Version: "+vers)
print ("Raw samples read = "+str(rawsamples))
print ("Accumulated Time offset = "+str(AccumTime))
print ("Processed Samples = "+str(numsamples)+"   Dropped outliers = "+str(dropped))
print ("Number of Time Intervals output = "+str(outputsamples))

