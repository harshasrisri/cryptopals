#!/bin/bash

runit () {
	echo
	challenge_number=$((challenge_number+1))
	echo "### Challenge $challenge_number"
	echo "\`\`\`"
	echo "python2 $@"
	python2 $@
	echo "\`\`\`"
}

challenge_number=0
echo "# Cryptopals Results"
echo
echo "## Set 1"
runit c1_hex2b64.py 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
runit c2_fixed_xor.py 1c0111001f010100061a024b53535009181c 686974207468652062756c6c277320657965
runit c3_onekeyxor.py 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
runit c4_detect_xor_string.py c4.txt 
runit c5_repeat_key_xor.py ICE c5.txt
runit c6_brk_rptkey_xor.py c6.txt
