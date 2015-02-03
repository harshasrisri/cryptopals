#!/usr/bin/python2
#Challenge 6, set 1, cryptopals.com

import sys, base64, itertools
from operator import itemgetter
from libcryptopal import *

def list_key_sizes (encr_text):
    """
    Returns a dictionary of key_size and normalized_edit_distance pairs sorted on edit_distances
    """
    return sorted (
            [(i, float(edit_distance (encr_text[0:i], encr_text[i:2*i])) / i) 
                for i in range (2, 41)], 
            key=itemgetter(1))

def guess_keyphrase (encr_text, keysize):
    """
    This function returns a keyphrase guessed from the given cryptotext and keysize
    """
    # First calculate the number of blocks of keysize length
    block_size = (len(encr_text) / keysize) + 1
    # Pad the string with appropriate number of NULs to form a blocksize multiple length string
    encr_text = encr_text.ljust(block_size * keysize, '\0')

    keyphrase = ''
    for i in range (0, keysize):
        line=''
        # Form a string of blocksize length to guess one character in keyphrase
        for j in range (0, block_size):
            line = line + encr_text[(j * keysize) + i]
        (key_char,weight) = guess_keychar (line)
        keyphrase = keyphrase + key_char
    return keyphrase

def main ():
    if len(sys.argv) != 2:
        print "Usage: " + sys.argv[0] + " <encrypted_file>"
        sys.exit()

    encr_text = open(sys.argv[1]).read().translate(None, '\n').decode('base64')
    key_sizes = list_key_sizes (encr_text)

    keyring = dict()
    for keysize, distance in key_sizes:
        keyphrase = guess_keyphrase (encr_text, keysize)
        keyring[keyphrase] = string_rank (keyphrase)
        print "keysize : %d \t distance : %f \t keyrank : %f \t keyphrase : %s" % (keysize, distance, string_rank(keyphrase) / keysize, keyphrase)

    # print max(keyring, key=keyring.get)

if __name__ == "__main__":
    main()
