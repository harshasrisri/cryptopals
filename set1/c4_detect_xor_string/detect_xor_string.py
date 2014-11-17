#!/usr/bin/python2

import sys
sys.path.insert (0,'../c3_onekeyxor')
import onekeyxor

def main () :
    maxrank = 0
    for line in open ('4.txt'):
        key,rank = onekeyxor.max_rank(line)
        if rank > maxrank:
            maxrank = rank
            maxkey = key
            maxline = line
    print ("%c : %d : %s") % (maxkey, maxrank, onekeyxor.xorstr(maxkey,maxline))
    return

if __name__ == "__main__":
    main()
