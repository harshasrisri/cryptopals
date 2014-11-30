#!/usr/bin/python2
#Challenge 6, set 1, cryptopals.com

import sys, base64, itertools
from operator import itemgetter
from edit_distance import edit_distance_of
sys.path.insert (0,'../c3_onekeyxor')
import onekeyxor

def guess_key_size (encr_text):
    return [(i, float(edit_distance_of (encr_text[0:i], encr_text[i:2*i])) / i) for i in range (2, 41)]

def break_with (encr_text, keysize):
    numblocks = len(encr_text) / keysize

    matrix = [encr_text[numblocks * i: numblocks * (i + 1)] for i in range(0, keysize)]
    if numblocks * keysize < len(encr_text): 
        matrix.append(encr_text[keysize * numblocks:])

    transpose = map(None, *matrix)

    keyword=''
    for row in transpose:
        try:
            encr_line = ''.join(row)
        except TypeError:
            encr_line = ''.join(row[:-1])
        key,rank = onekeyxor.max_rank(encr_line.encode('hex'))
        keyword = keyword + key

    print keyword

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
