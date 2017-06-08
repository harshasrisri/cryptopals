#!/usr/bin/python2
import sys
import string
from libcryptopal import *

def main ():
    if len(sys.argv) != 2:
        print ("usage: " + sys.argv[0] + " <hex_string>")
        sys.exit()

    msg = sys.argv[1].decode('hex')
    maxkey,result=guess_keychar(msg)
    print ("%c : %s") % (maxkey, xorstr(maxkey, msg))

if __name__ == "__main__":
    main()
