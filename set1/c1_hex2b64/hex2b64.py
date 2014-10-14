#!/usr/bin/python
import sys

if len(sys.argv) != 2:
	print "usage: %s <hex_number>" % sys.argv[0]
	sys.exit()

print "%X" % int(sys.argv[1], 16)

