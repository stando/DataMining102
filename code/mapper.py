#!/usr/bin/env python2.7

import numpy as np
import random
import sys

lam = 0.1
nt = 10
#nlen = 80600
nlen = 160400
#nlen = 800
w = np.zeros(nlen)

# This function has to either stay in this form or implement the
# feature mapping. For details refer to the handout pdf.
def transform(x_original):
    y_original = x_original
    for x in range(0,400,1):
        z_original = np.multiply(x_original, x_original[x])
        y_original = np.concatenate((y_original, z_original), axis=0)
    """
    y_original = x_original
    for x in range(0,400,1);
        z_original = np.multiple(x_original)
        y_original = np.concatenate((x_original, y_original), axis=0)
    """
    """
    y_original = x_original
    for x in range(0,400,1):
        for y in range(x,400,1):
            y_original = np.append(y_original,[x_original[x]*x_original[y]])
    """
    return y_original

if __name__ == "__main__":
    np.random.seed(seed=42)

    for line in sys.stdin:
        line = line.strip()
        count = 0
        feature = []
        label = int(line[:2])
        fea = np.fromstring(line[3:],sep=" ")
        feature = transform(fea)
        sign = 0
        for i in range(0,nlen,1):
            sign += float(feature[i])*w[i]
        loss = label * sign
        #update w
        if loss < 1:
            s = 0
            wp = w
            for i in range(0,nlen,1):
                wp[i] = w[i] + nt * label * float(feature[i])
                s = s + wp[i] * wp[i]
            if np.sqrt(lam*s) > 1:
                for i in range(0,nlen,1):
                    w[i] = wp[i]
            else:
                for i in range(0,nlen,1):
                    w[i] = wp[i] * 1/np.sqrt(lam*s)
    for i in range(0, nlen,1):
        print "%d\t%f" % (i, w[i])
