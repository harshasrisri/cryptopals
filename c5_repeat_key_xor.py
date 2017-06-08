#!/usr/bin/python2
import sys
from libcryptopal import *

def main ():
    if len(sys.argv) != 3:
        print ("Usage: " + sys.argv[0] + " <key_phrase> <textfile>")
        sys.exit()

    with open (sys.argv[2]) as input_file:
        line = input_file.read()

    # for line in open(sys.argv[2]):
    cryptline = xorstr (sys.argv[1], line.strip()).encode('base64')
    print (cryptline)

    return

if __name__ == "__main__":
    main()
