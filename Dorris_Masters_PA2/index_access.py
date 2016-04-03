#!/usr/bin/python

import re

filename="index.txt"

f = open(filename, "r")

file_contents = []
d = {}

for line in f:
        line = line.strip('\n')
	line = line.split('\t')# = line.strip('\n').replace('\t',' ')
	current_key = line[0]
        d[current_key] = []
	for s in line[1].split(';')[:-1]:
	    d[current_key].append(s.replace('(','').replace(')','').split(','))

exit_status = False

while not exit_status:
	query = raw_input("Enter word: ")
	if query == "exit" or query == "Exit" or query == "EXIT":
		exit_status = True
	elif not query in d.keys():
		print "Word not in index"		
	else:
		print "%s->" % query, 
		for s in d[query]:
			print "%s" % s,
		print '\n\n'
