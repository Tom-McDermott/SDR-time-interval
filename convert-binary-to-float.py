#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:48:02 2015

@author: Tom McDermott, N5EG
"""

#Read a file with 4-byte (32 bit) floating point numbers and
#output a one-column list to a file

import struct

numsamples = 0

file = open("tie-vector")
file2 = open("tie_vec_outfile", 'w')

while file:
    inbin = file.read(4)
    if not inbin:
        break
    val = struct.unpack('f', inbin)[0]
    file2.write(str(val)+'\n')
    numsamples+=1

file.close
file2.flush()
file2.close

print "Processed Samples =   ",numsamples
    
