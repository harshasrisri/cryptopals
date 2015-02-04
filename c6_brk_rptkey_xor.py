#!/usr/bin/python2
#Challenge 6, set 1, cryptopals.com

import sys, base64, itertools
from operator import itemgetter
from libcryptopal import *

def main ():
    if len(sys.argv) != 2:
        print "Usage: " + sys.argv[0] + " <encrypted_file>"
        sys.exit()

    encr_text = open(sys.argv[1]).read().translate(None, '\n').decode('base64')
    key_distances = sorted (get_key_distances (encr_text, 2, 41), key=itemgetter(1))

    keyring = dict()
    for keysize, distance in key_distances:
        keyphrase = guess_keyphrase (encr_text, keysize)
        keyring[keyphrase] = string_rank (keyphrase)
        print "keysize : %d \t distance : %f \t keyrank : %f \t keyphrase : %s" % \
                (keysize, distance, string_rank(xorstr(keyphrase,encr_text)) / keysize, keyphrase)

    # print xorstr ('Terminator X: Bring the noise', encr_text)

if __name__ == "__main__":
    main()
