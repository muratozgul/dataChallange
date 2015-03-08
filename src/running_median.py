#!/usr/bin/env python

#murat running median
import sys
from heapq import heappush as push, heappushpop as pushpop
 
def smedian():
    def gen():
        left, right = [], [(yield)]
        while True:
            push(left,  -pushpop(right, (yield right[0])))
            push(right, -pushpop(left, -(yield ((right[0] - left[0])/2.0))))
    g = gen()
    next(g)
    return g
 
# an example:
mediansofar = smedian()
 
for line in sys.stdin:
	size = len(line.split())
	#print("size: " + str(size))
	print mediansofar.send(size)