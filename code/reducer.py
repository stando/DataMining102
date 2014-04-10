#!/usr/bin/env python2.7

import sys
import numpy as np

w = []
num = 0
#nlen = 800
nlen = 400
#last_key = None
le = [0 for j in range(nlen)]
d =[[0 for j in range(50)] for i in range(nlen)]


if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        key, x = np.fromstring(line,sep="\t")
        key = int(key)
        le[key] = le[key] + 1
        d[key][le[key]] = float(x)
        """
        if last_key is None:
            last_key =  key
        if key == last_key:
            d[key].append(x)
        else:
            last_key = key
        """
    for i in range(0,nlen,1):
        s = 0.0
        #print "%d %d" %(i, le[i])
        for j in range(1, le[i]+1,1):
            s = s + d[i][j]
        s /= le[i]
        print "%f " % s,
    print "\n"



