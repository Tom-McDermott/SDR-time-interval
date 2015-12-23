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

1. Run the flowgraph. It produces a binary output file
tie-vector.
2. Run the convert-binary-to-float.py program. It
converts tie-vector to tie_vec_outfile to ASCII.
3. Run convert-fast-tie-to-TimeInterval.py program.
It converts the over-sampled time intervals to one
sample per second TimeIntervals file.
4. This can be directly processed by Tom Van Baak's
Adev.c program to produce Allan Deviation.

