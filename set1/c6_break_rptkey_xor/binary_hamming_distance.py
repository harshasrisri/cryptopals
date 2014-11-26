#!/usr/bin/python2

import sys, binascii

def binary_hamming_distance_of (str1, str2):
    """
    Calculates the Hamming distance of 2 strings after converting them to ascii-decoded binary strings
    """
    str1.strip()
    str2.strip()
    if len(str1) != len(str2):
        print "Strings have to be of equal lengths: " + str1 + " and " + str2
        return -1

    ham1 = bin(int(binascii.hexlify(str1),16))
    ham2 = bin(int(binascii.hexlify(str2),16))

    return sum(True for i in range (0, len(ham1)) if ham1[i] != ham2[i])

def main ():
    if len(sys.argv) == 3:
        str1 = sys.argv[1]
        str2 = sys.argv[2]
    else:
        str1 = "test string"
        str2 = "TEST STRING"

    print ("Hamming distance of '%s' and '%s' is %d") % (str1, str2, binary_hamming_distance_of(str1, str2))

if __name__ == "__main__":
    main()
