#!/usr/bin/env python

# murat ozgul - word_count reducer

import sys

current_word = None
word_count = 0
word = None

for line in sys.stdin:
    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # discard
        continue

    if current_word == word:
        word_count += count
    else:
        if current_word:
            print '%s\t%s' % (current_word, word_count)
        word_count = count
        current_word = word

# output the last word
if current_word == word:
    print '%s\t%s' % (current_word, word_count)