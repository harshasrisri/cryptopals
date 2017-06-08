#!/usr/bin/python
import sys
import base64

if len(sys.argv) != 2:
    print "usage: %s <hex_number>" % sys.argv[0]
    sys.exit()

hex_num = sys.argv[1].decode('hex').strip()
b64_num = hex_num.encode('base64').strip()

print "%s %s" % (b64_num, hex_num)
