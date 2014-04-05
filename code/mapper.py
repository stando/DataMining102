#!/usr/bin/env python2.7

import numpy as np
import random
import sys

w = np.zeros(400)
lam = 0.1
nt = 10

# This function has to either stay in this form or implement the
# feature mapping. For details refer to the handout pdf.
def transform(x_original):
    return x_original

if __name__ == "__main__":
    np.random.seed(seed=42)

    for line in sys.stdin:
        line = line.strip()
        count = 0
        feature = []
        label = int(line[:2])
        feature = np.fromstring(line[3:],sep=" ")
        sign = 0
        for i in range(0,400,1):
            sign += float(feature[i])*w[i]
        loss = label * sign
        #update w
        if loss < 1:
            s = 0
            wp = w
            for i in range(0,400,1):
                wp[i] = w[i] + nt * label * float(feature[i])
                s = s + wp[i] * wp[i]
            if np.sqrt(lam*s) > 1:
                for i in range(0,400,1):
                    w[i] = wp[i]
            else:
                for i in range(0,400,1):
                    w[i] = wp[i] * 1/np.sqrt(lam*s)
    for i in range(0,400,1):
        print "%f " % w[i],
    print "\n"
