#!/usr/bin/python
import sys

if len(sys.argv) != 3:
	print "usage %s <hex_num> <hex_num>" % sys.argv[0]
	sys.exit()

if len(sys.argv[1]) != len(sys.argv[2]):
	print "inputs should be of equal length"
	sys.exit()

num1 = int(sys.argv[1], 16)
num2 = int(sys.argv[2], 16)
print "%X xor %X = %X" % (num1, num2, num1 ^ num2)
