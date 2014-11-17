#!/usr/bin/python2

import sys
sys.path.insert (0,'../c3_onekeyxor')
import onekeyxor

def main () :
    if len(sys.argv) != 2:
        print ("Usage: " + sys.argv[0] + " <file with ciphertext>")
        sys.exit()

    maxrank = 0
    for line in open (sys.argv[1]):
        key,rank = onekeyxor.max_rank(line)
        if rank > maxrank:
            maxrank = rank
            maxkey = key
            maxline = line
    print ("%c : %d : %s") % (maxkey, maxrank, onekeyxor.xorstr(maxkey,maxline))
    return

if __name__ == "__main__":
    main()
