#!/usr/bin/python2
import sys

def repeat_encrypt (keyword, line):
    cryptline = ""
    line = line.strip()
    modcount = 0
    for char in line:
        cryptline += "%02x" % (int(keyword[modcount].encode('hex'), 16) ^ int(char.encode('hex'), 16))
        modcount = (modcount + 1) % len(keyword)

    return cryptline

def main ():
    if len(sys.argv) != 3:
        print ("Usage: " + sys.argv[0] + " <key_phrase> <textfile>")
        sys.exit()

    print ("Keyword: " + sys.argv[1])
    with open (sys.argv[2]) as input_file:
        line = input_file.read()

    # for line in open(sys.argv[2]):
    cryptline = repeat_encrypt (sys.argv[1], line)
    print ("Plaintext line: " + line)
    print ("Encrypted line: " + cryptline)

    return

if __name__ == "__main__":
    main()
