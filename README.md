Time Interval Measurements using SDR
====================================

This repository contains a Gnuradio grc file
and some python helper utilities for capturing
and formatting Time Interval measurements that
are normally used in Allan Deviation or similar
stability measurements.

The GRC file references the Hermes SDR radio,
but it is easy to replace. The sample rate is set
at 48000 s/s, and is a parameter.

One python file converts the binary file created
by gnuradio to ASCII text, while the other tranlates
the time measuremetns to time intervals and also
throws out outlier samples.

The time interval converter narrowly bounds where
samples must be to survive. This is due to a problem
with the specific SDR being used (a random glitch).
You can open up the allowed range by latering the
python code.

Expect these files to change frequently for awhile.

