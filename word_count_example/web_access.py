#!/usr/bin/python
#web_access.py

import re
from operator import itemgetter

def multiple_words(l, lookup):
	tmp = []
	for w in l:
		if w in lookup:
			tmp.append(lookup[w])
		else:
			tmp = []
			break
	flag = True
	index=tmp[0]
	for i in tmp[1:]:
		if not int(index[0][2])+1 == int(i[0][2]):
			flag = False
		index = i
	if flag:
		return tmp[0]
	else:
		return []

def and_f(l, lookup, tmp_result, not_tmp,first):
	if l[0].lower() == 'not' and not first:
		ttmp_result, tnot_tmp = and_f(l[1:],lookup,tmp_result,not_tmp,False)
		not_tmp.extend(ttmp_result)
	elif l[0].lower() == 'not' and first:
		ttmp_result, tnot_tmp = and_f(l[1:],lookup,tmp_result,not_tmp,True)
	else:
		word = l[0]	
		if len(l)>1:
			and_result=multiple_words(l,lookup)	
		else:
			if not word in lookup:
				and_result = []
			else:
				and_result=lookup[word]
		rr = []
		if first:
			tmp_result = lookup[word]
		else:
			for s1 in and_result:
				for s2 in tmp_result:
					if int(s1[1]) == int(s2[1]):
						rr.append(s1)
			tmp_result = rr
	return tmp_result, not_tmp

def or_f(l, lookup, tmp_result, not_tmp):
	if l[0].lower() == 'not':
		ttmp_result, tnot_tmp = or_f(l[1:],lookup,tmp_result,not_tmp)
		not_tmp.extend(ttmp_result)
	elif len(l) > 1:
		tmp_result.extend(multiple_words(l,lookup))
	else:
		if l[0] in lookup:
			tmp_result.extend(lookup[l[0]])
	return tmp_result, not_tmp

filename="index_pos.txt"

f = open(filename, "r")

file_contents = []
d = {}

for line in f:
        line = line.strip('\n')
	line = line.split('\t')
	current_key = line[0]
        d[current_key] = []
	for s in line[1].split(';')[:-1]:
	    d[current_key].append(s.replace('(','').replace(')','').split(','))

exit_status = False

line_numbers = []
not_line_numbers = []
tmp_list =[]
processing_list=[]

query = raw_input("Ready:")
string = query
query = query.split()

cut_flag = False

for word in query:
	if cut_flag == False:
		cut_flag = True
		tmp_list.append(word)
	elif cut_flag == True and not (word.lower() == 'or' or word.lower() == 'and'):
		tmp_list.append(word)
	else:
		processing_list.append(tmp_list)
		tmp_list = []
		tmp_list.append(word)

processing_list.append(tmp_list)

for l in processing_list:
	if l[0] == 'and':
		line_numbers, not_line_numbers = and_f(l[1:],d, line_numbers, not_line_numbers,False)
	elif l[0] == 'or':
		line_numbers, not_line_numbers = or_f(l[1:],d, line_numbers, not_line_numbers)
	else:
		line_numbers, not_line_numbers = and_f(l,d, line_numbers, not_line_numbers,True)

for l in line_numbers:
	if not l in not_line_numbers:
		print l
