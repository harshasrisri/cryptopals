#!/usr/bin/python2
#Challenge 6, set 1, cryptopals.com

import sys, base64, itertools
from operator import itemgetter
from libcryptopal import *
import timeit

def main ():
    infile = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin

    encr_text = infile.read().replace('\n','').decode('base64')

    maxrank = 0
    for keysize, distance in get_key_distances (encr_text, 2, 64):
        keyphrase = guess_keyphrase (encr_text, keysize)
        keyrank = string_rank (xorstr (keyphrase, encr_text))
        if keyrank > maxrank:
            maxrank = keyrank
            maxkey = keyphrase
            # print "Updated values - %02d : %d : %s" % (keysize, keyrank, keyphrase)
    
    print maxkey

if __name__ == "__main__":
    # print timeit.timeit(main,number=1)
    main()
