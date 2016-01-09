Time Interval Measurements using SDR
====================================

This repository contains a Gnuradio grc file
and some python helper utilities for capturing
and formatting Time Interval measurements that
are normally used in Allan Deviation or similar
stability measurements.


Copyright 2015, Thomas C. McDermott, N5EG.
Contents are licensed under the GNU Public License,
version 2.0, or at your option any later version.


The GRC file references the Hermes SDR radio,
but it is easy to replace. The sample rate is set
at 48000 s/s, and is a parameter. It can be changed.

One python file converts the binary file created
by gnuradio to ASCII floating point text, while the
other tranlates the time measurements to time
intervals and also throws out outlier samples.

The time interval converter narrowly bounds where
samples must be to survive. This is due to a problem
with the specific SDR being used (a random glitch).
You can open up the allowed range by changing the
python code.

Expect these files to change frequently for awhile.

1. The flowgraph has been replaced by one that uses
strictly integer math to timestamp the zerocrossings.
Gnuradio uses single-point floats which causes Allan
Deviation background noise of about 1E-14 at tau=1
second.

2. Run the convert-int/combo.py program. It reads the
binary values produced by Gnuradio into integers then
computes the time intervals, and reformats to floats.
The program has hardcoded the sample rate at 48000 samp/sec.
If you sample at a different rate, you will need to change
one line in this converter.

3. You may wish to run the Python program Min-and-Max-
from-TimeInterval.py.  It will print the mean, minimum,
and maximum Time Intervals. This will help you see
if there are any outliers in the file.

4. The TimeInterval file can be diretly processed
by Tom Van Baak's Adev.c program to produce Allan Deviation.
For my setup the command was:
$ ./Adev 1 1e-9 < TimeIntervals
This means one measurement per second, each unit equal to one
nanosecond.

