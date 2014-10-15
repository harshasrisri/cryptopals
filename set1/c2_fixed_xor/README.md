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
