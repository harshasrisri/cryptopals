#!/usr/bin/python
import sys
import base64

if len(sys.argv) != 2:
	print "usage: %s <hex_number>" % sys.argv[0]
	sys.exit()

# hex_num = int(sys.argv[1], 16)
hex_num = sys.argv[1].decode('hex')
b64_num = hex_num.encode('base64')

print "Decoded hex: " + hex_num
print "Encoded B64: " + b64_num
