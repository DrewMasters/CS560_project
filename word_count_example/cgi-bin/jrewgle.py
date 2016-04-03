#!/usr/bin/python

import cgi, cgitb
import re


print "Content-type:text/html\r\n\r\n"
#print "<html>"
#print "<head>"
#print "<title>Hello - Second CGI Program</title>"
#print "</head>"
#print "<body>"
#print "<h2>Hello %s</h2>" % (query)
#print "</body>"
#print "</html>"

length = 0
query = ""
results = []

form = cgi.FieldStorage()

query = form.getvalue('query')
#query_split = query.split(" ")

filename="index_pos.txt"

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

#query = query.lower()

if query in d.keys():
  results = d[query] 

#if 'REQUEST_METHOD' in os.environ.keys() and os.environ['REQUEST_METHOD']=="POST":
#  length = int(os.environ['CONTENT_LENGTH'])
#  query = sys.stdin.read(int(os.environ['CONTENT_LENGTH'])).split('&')
#  for i in range(0,len(query#)):
#    query[i] = "new"

print """<!DOCTYPE html>
<html>
<p> JREWGLE </p>
<head>
  <title>JREWGLE</title>
  <meta charset="UTF-8">
</head>

<form action="http://localhost:8080/cgi-bin/jrewgle.py" method="post">
Search: <input type="text" name="query"><br />
<input type="submit" value="Submit" />
</form>

<p> Query = %s</p>""" % query

for i in range(0,len(results)):
  print "<p> Doc1, line %s </p>" % results[i][1]

print """
</body>
</html>"""
