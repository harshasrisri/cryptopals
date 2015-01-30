#!/usr/bin/python2

import sys, binascii
from libcryptopal import *

def main ():
    if len(sys.argv) == 3:
        str1 = sys.argv[1]
        str2 = sys.argv[2]
    else:
        str1 = "test string"
        str2 = "TEST STRING"

    print ("Hamming distance of '%s' and '%s' is %d") % (str1, str2, edit_distance_of(str1, str2))

if __name__ == "__main__":
    main()
