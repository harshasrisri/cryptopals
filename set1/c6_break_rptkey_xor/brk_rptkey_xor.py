#!/usr/bin/python2
#Challenge 6, set 1, cryptopals.com

import sys, base64
from operator import itemgetter
from edit_distance import edit_distance_of

def guess_key_size (encr_text):
    return [(i, float(edit_distance_of (encr_text[0:i], encr_text[i:2*i])) / i) for i in range (2, 41)]

def break_with (encr_text, keysize):
    block_size = len(encr_text) / keysize

    matrix = [encr_text[block_size * i: block_size * (i + 1)] for i in range(0, keysize)]
    if block_size * keysize < len(encr_text): 
        matrix.append(encr_text[keysize * block_size:])

    print ("%d : %d : %d : %d") % (len(encr_text), keysize, block_size, len(matrix))

    # for i in range(0, len(matrix[-1])):
        

def main ():
    if len(sys.argv) != 2:
        print "Usage: " + sys.argv[0] + " <encrypted_file>"
        sys.exit()

    encr_text = open(sys.argv[1]).read().translate(None, '\n').decode('base64')
    key_sizes = guess_key_size(encr_text)
    key_sizes = sorted (key_sizes, key=itemgetter(1))

    for keysize, distance in key_sizes:
        if distance < 3:
            print "Breaking with " + str(keysize) + " : " + str(distance)
            break_with (encr_text, keysize)

if __name__ == "__main__":
    main()
