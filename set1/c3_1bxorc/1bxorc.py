#!/usr/bin/python
import sys
import string

def xorstr (key, msg):
	temp_str = ""
	for in_char in msg:
		temp_str += chr(ord(in_char) ^ ord(key))
	return temp_str

if len(sys.argv) != 2:
	print "usage: %s <hex_string>" % sys.argv[0]
	sys.exit()

msg = sys.argv[1].decode('hex')
freq_set = "etaoin shrdlu"
results = dict()

for key in string.ascii_letters:
	rank = 0
	plaintext = xorstr(key, msg)
	for letter in plaintext:
		if letter in freq_set:
			rank = rank + 1
	results[key] = rank

maxkey = [x for x,y in results.items() if y == max(results.values())]
print "%c : %d : %s" % (maxkey[0], results[maxkey[0]], xorstr(maxkey[0], msg))
