#!/usr/bin/env python2.7

import sys
import numpy as np

w = []

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        x = np.fromstring(line,sep=" ")
        w.append(x)
    wei = w.mean(0)
    for i in range(0,400,1):
        s = 0
        for j in range(0,10,1):
            s = s + wei[j][i]
        s /= 10
        print "%f\n" % s



