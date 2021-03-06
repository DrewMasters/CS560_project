#!/usr/bin/env python

# Use the sys module
import sys
import string

# 'file' in this case is STDIN
def read_input(file):
    # Split each line into words
    for line in file:
        line = line.lower()
        for c in string.punctuation:
            line = line.replace(c,"")
        yield line.split()

def main(separator='\t'):

    stop_words = ['the','and','i','to','of','a','you','my','that','in','is','not','for','with','me','it','be','this','your','his','but','he','as','have','thou','so','him','will','what','by','thy','all','are','her','no','do','shall','if','we','or']

    # Read the data using read_input
    data = read_input(sys.stdin)
    flag = 1
    pos = 0
    fn  = 0
    # Process each words returned from read_input
    for words in data:
        pos = 0
        # Process each word
        for word in words:
            if flag==1:
              fn = word
              flag = 2
            elif flag==2:
              num = word
              flag = 0
            else:
              # Write to STDOUT
              if not word in stop_words:
                print '%s%s%s%s%s%s%d' % (word, separator, fn, separator, num, separator, pos)
            pos=pos+1
        flag=1

if __name__ == "__main__":
    main()
