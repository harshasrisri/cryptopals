#Cryptopals Results

##Set 1

###C1
```
python2 c1_hex2b64.py 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
Decoded hex: I'm killing your brain like a poisonous mushroom
Encoded B64: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

```

###C2
```
python2 c2_fixed_xor.py 1c0111001f010100061a024b53535009181c 686974207468652062756c6c277320657965
1C0111001F010100061A024B53535009181C xor 686974207468652062756C6C277320657965 = 746865206B696420646F6E277420706C6179
```

###C3
```
python2 c3_onekeyxor.py 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
X : 208 : Cooking MC's like a pound of bacon
```

###C4
```
python2 c4_detect_xor_string.py c4.txt
5 : 198 : Now that the party is jumping

```

###C5
```
python2 c5_repeat_key_xor.py ICE c5.txt
Keyword: ICE
Plaintext line: Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal

Encrypted line: 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
```
