#!/usr/bin/env python

# import modules
from itertools import groupby
from operator import itemgetter
import sys

# 'file' in this case is STDIN
def read_mapper_output(file, separator='\t'):
    # Go through each line
    for line in file:
        # Strip out the separator character
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    index = {}
    # Read the data using read_mapper_output
    data = read_mapper_output(sys.stdin, separator=separator)
    # Group words and counts into 'group'
    #   Since MapReduce is a distributed process, each word
    #   may have multiple counts. 'group' will have all counts
    #   which can be retrieved using the word as the key.
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            #if not current_word in index:
            index[current_word] = []
            for current_word, info in group:
              index[current_word].append(info.split(separator))
            #else:
            #  dict[current_word].append()
              
            # For each word, pull the count(s) for the word
            #   from 'group' and create a total count
            #total_count = sum(int(count) for current_word, count in group)
            # Write to stdout
            print "%s%s" % (current_word,separator),
            for i in index[current_word]:
              sys.stdout.write("(%s,%s,%s);" % (i[0],i[1],i[2]))
            print ""
        except ValueError:
            # Count was not a number, so do nothing
            pass

if __name__ == "__main__":
    main()
