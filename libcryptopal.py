"""
Python source file containing helper functions for the cryptopals exercise
"""
import sys
import string
import binascii

def xorstr (key, msg):
    """
    This function takes a one byte key and a multi-byte hex-encoded string as a message. 
    It returns a string that is obtained by XORing the key with each byte of the message.
    """
    msg = msg.strip();
    msg = msg.decode('hex')
    xor_str = ""
    for in_char in msg:
        xor_str += chr(ord(in_char) ^ ord(key))
    return xor_str

def guess_key (msg):
    """
    This function takes an XOR-encrypted string as argument and tries to guess which 
    among the printable characters could be used as a key to XOR a plaintext string. 
    """
    freq_set = { 
            ' ':13.00, 'e':12.70, 't':9.056, 'a':8.167, 'o':7.507, 'i':6.966, 'n':6.749, 
            's':6.327, 'h':6.094, 'r':5.987, 'd':4.253, 'l':4.025, 'u':2.758, 'b':1.492, 
            'c':2.782, 'f':2.228, 'g':2.015, 'j':0.153, 'k':0.772, 'm':2.406, 'p':1.929, 
            'q':0.095, 'v':0.978, 'w':2.360, 'x':0.150, 'y':1.974, 'z':0.074 }
    results = dict()
    for key in string.printable:
        rank = 0
        plaintext = xorstr(key, msg)
        for letter in plaintext:
            if letter in freq_set:
                rank = rank + freq_set[letter]
        results[key] = rank
    maxkey = [x for x,y in results.items() if y == max(results.values())]
    return (maxkey[0],results[maxkey[0]])

def edit_distance (str1, str2):
    """
    This function calculates the binary Hamming distance of 2 strings by converting 
    them to ascii-decoded binary strings. For example, the distance between:
            this is a test
    and 
            wokka wokka!!!
    is 37. Note that the length of the strings should be equal
    """
    str1.strip()
    str2.strip()
    if len(str1) != len(str2):
        raise ValueError("Strings have to be of equal lengths: " + str1 + " and " + str2)

    # get the hex values of each character in the string, convert it into a a hex integer
    # and convert it into a binary string and strip the leading 0b indicating the base 2
    ham1 = bin(int(binascii.hexlify(str1),16))[2:]
    ham2 = bin(int(binascii.hexlify(str2),16))[2:]

    if len(ham1) < len(ham2): ham1 = '0' + ham1
    if len(ham2) < len(ham1): ham2 = '0' + ham1

    return sum(True for i in range (0, len(ham1)) if ham1[i] != ham2[i])

def repeating_key_encrypt (keyword, line):
    """
    This function takes a keyword and a message of arbitrary lengths. The message is XOR-
    encrypted with the character obtained by cycling through the keyword.
    """
    cryptline = ""
    line = line.strip()
    modcount = 0
    for char in line:
        cryptline += "%02x" % (int(keyword[modcount].encode('hex'), 16) ^ int(char.encode('hex'), 16))
        modcount = (modcount + 1) % len(keyword)
    return cryptline

