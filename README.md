Cryptopals
==

This is a repo containing exercises from http://cryptopals.com/. The site hosts quite a few problems which originated in the Matasano Crypto Challenges. Please read the link for complete description
Hex to Base64 convertor
==

This is a small python script to convert an arbitrarily long hex string to a base 64 string

```
./hex2b64.py 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
Decoded hex: I'm killing your brain like a poisonous mushroom
Encoded B64: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
```
Fixed XOR
==

Write a function that takes two equal-length buffers and produces their XOR combination. If your function works properly, then when you feed it the string:

```
1c0111001f010100061a024b53535009181c
```

after hex decoding, and when XOR'd against:
```
686974207468652062756c6c277320657965
```

should produce:
```
746865206b696420646f6e277420706c6179
```

Here is the final result:
```
./fixed_xor.py 1c0111001f010100061a024b53535009181c 686974207468652062756c6c277320657965
1C0111001F010100061A024B53535009181C xor 686974207468652062756C6C277320657965 = 746865206B696420646F6E277420706C6179
```
Single-byte XOR cipher
==

The hex encoded string:

```
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
```

has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score. 

Results:

```
./1bxorc.py 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
X : 23 : Cooking MC's like a pound of bacon
```
Detect single-character XOR
==

One of the 60-character strings in [this file](4.txt) has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)

Results:
~~~
./detect_xor_string.py 4.txt 
5 : 198 : Now that the party is jumping
~~~
Implement repeating-key XOR
===

Here is the opening stanza of an important work of the English language:

~~~
Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal
~~~

Encrypt it, under the key "ICE", using repeating-key XOR.

In repeating-key XOR, you'll sequentially apply each byte of the key; the first byte of plaintext will be XOR'd against I, the next C, the next E, then I again for the 4th byte, and so on.

It should come out to:

~~~
0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
~~~

Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt your mail. Encrypt your password file. Your .sig file. Get a feel for it. I promise, we aren't wasting your time with this.

Result:
~~~
./repeat_key_xor.py ICE input
Keyword: ICE
Plaintext line: Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal

Encrypted line: 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
~~~
Break repeating-key XOR
===

Read the problem [here](http://cryptopals.com/sets/1/challenges/6/)
