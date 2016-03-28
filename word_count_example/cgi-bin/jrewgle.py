#!/usr/bin/python

import cgi, cgitb

form = cgi.FieldStorage()

query = form.getvalue('query')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print "<h2>Hello %s</h2>" % (query)
print "</body>"
print "</html>"
