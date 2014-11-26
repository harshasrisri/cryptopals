#!/usr/bin/python2

import sys, binascii

def hamming_distance_of (str1, str2):
    str1.strip()
    str2.strip()
    if len(str1) != len(str2):
        print "Strings have to be of equal lengths: " + str1 + " and " + str2
        return -1

    ham1 = bin(int(binascii.hexlify(str1),16))
    ham2 = bin(int(binascii.hexlify(str2),16))

    print str1 + " : " + ham1
    print str2 + " : " + ham2

    distance = 0
    for i in range(0, len(ham1)):
        if ham1[i] != ham2[i]:
            distance = distance + 1

    return distance

def main ():
    if len(sys.argv) == 3:
        str1 = sys.argv[1]
        str2 = sys.argv[2]
    else:
        str1 = "test string"
        str2 = "TEST STRING"

    distance = hamming_distance_of (str1, str2)
    print ("Hamming distance of '%s' and '%s' is %d") % (str1, str2, distance)

if __name__ == "__main__":
    main()
