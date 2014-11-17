#!/usr/bin/python2
import sys
import string

freq_set = { ' ':13, 'e':12.702, 't':9.056, 'a':8.167, 'o':7.507, 'i':6.966, 'n':6.749, 's':6.327, 'h':6.094, 'r':5.987, 'd':4.253, 'l':4.025, 'u':2.758, 'b':1.492, 'c':2.782, 'f':2.228, 'g':2.015, 'j':0.153, 'k':0.772, 'm':2.406, 'p':1.929, 'q':0.095, 'v':0.978, 'w':2.360, 'x':0.150, 'y':1.974, 'z':0.074 }

keyspace = string.ascii_letters + string.digits

results = dict()

def xorstr (key, msg):
    msg = msg.strip();
    msg = msg.decode('hex')
    xor_str = ""
    for in_char in msg:
        xor_str += chr(ord(in_char) ^ ord(key))
    return xor_str

def max_rank (msg):
    for key in keyspace:
        rank = 0
        plaintext = xorstr(key, msg)
        for letter in plaintext:
            if letter in freq_set:
                rank = rank + freq_set[letter]
        results[key] = rank
    maxkey = [x for x,y in results.items() if y == max(results.values())]
    return (maxkey[0],results[maxkey[0]])

def main ():
    if len(sys.argv) != 2:
        print ("usage: " + sys.argv[0] + " <hex_string>")
        sys.exit()

    msg = sys.argv[1]
    maxkey,result=max_rank(msg)
    print ("%c : %d : %s") % (maxkey, result, xorstr(maxkey, msg))

if __name__ == "__main__":
    main()
