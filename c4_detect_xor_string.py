#!/usr/bin/python2

import sys
from libcryptopal import *

def main () :
    if len(sys.argv) != 2:
        print ("Usage: " + sys.argv[0] + " <file with ciphertext>")
        sys.exit()

    maxrank = 0
    for line in open (sys.argv[1]):
        line = line.strip()
        line = line.decode('hex')
        key,rank = guess_keychar(line)
        if rank > maxrank:
            maxrank = rank
            maxkey = key
            maxline = line
    print ("%c : %d : %s") % (maxkey, maxrank, xorstr(maxkey,maxline))
    return

if __name__ == "__main__":
    main()
