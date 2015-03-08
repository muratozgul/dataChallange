#!/usr/bin/env bash

# load all dependencies
# no dependencies

# make sure that all my programs (written in Python in this example) have the proper permissions
chmod +x ./src/word_count_mapper.py
chmod +x ./src/word_count_reducer.py
chmod +x ./src/running_median.py

# execute programs, with the input directory wc_input and output the files in the directory wc_output
# word count
cat ./wc_input/* | ./src/word_count_mapper.py | sort | ./src/word_count_reducer.py > ./wc_output/wc_result.txt
# running median
cat ./wc_input/* | ./src/running_median.py > ./wc_output/med_result.txt



