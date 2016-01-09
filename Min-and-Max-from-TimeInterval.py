#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 12:50:00 2015

@author: Tom McDermott, N5EG
"""

#Find the min, max, and mean from a TimeInterval file.


file = open("TimeIntervals", 'r')

Tprev = float(file.readline())

Min = 200.0
Max = -200.0
Mean = 0.0
Numsamples = 0


while file:
    instring = file.readline()
    if not instring:
        break

    Tnext = float(instring)
    Tdelta = Tnext - Tprev + 100.0
    Tprev = Tnext
   
    if Tdelta < Min:
        Min = Tdelta
        
    if Tdelta > Max:
        Max = Tdelta

    Mean += Tdelta

    Numsamples +=1     
 
Mean = Mean/float(Numsamples)
 
print ("Minimum = ",Min,"  Maximum = ",Max,"   Mean = ",Mean,"   Number of samples = ",Numsamples)
 
file.close


 
