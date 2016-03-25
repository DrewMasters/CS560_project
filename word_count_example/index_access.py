#!/usr/bin/python

import re

filename="index.txt"

f = open(filename, "r")

file_contents = []
d = {}

for line in f:
	line = line.strip('\n').replace('\t','')
	flag=0
	current_key = ""
	for s in line.split():
		if flag == 0:
			flag = 1
			current_key = s
			d[s] = []
		else:
			d[current_key].append(s)

exit_status = False

while not exit_status:
	query = raw_input("Enter word: ")
	if query == "exit" or query == "Exit" or query == "EXIT":
		exit_status = True
	elif not query in d.keys():
		print "Word not in index"		
	else:
		print "Word appears in lines: ", 
		for s in d[query]:
			print s,
		print '\n\n'
