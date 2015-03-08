#!/usr/bin/env python

# murat ozgul - word_count mapper
import sys, re, string

regex = re.compile('[%s]' % re.escape(string.punctuation))

for line in sys.stdin:
    
    # remove leading and trailing whitespace and punctuation
    line = regex.sub('', line.strip())
    
    # split the line into words
    words = line.split()
    
    # increase counters
    for word in words:
        print '%s\t%s' % (word, 1)