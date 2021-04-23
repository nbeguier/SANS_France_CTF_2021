# Crypto 05

We have managed to recover 2 encrypted files and we need you to crack them. Also we managed to find a version of one of the files before it was encrypted and we believe it uses the same key. See if you can use this to decrypt the 'sample.enc' file. Grab the files at https://xxxxxxxxxx/ch02.zip

## Solution

`crypt1.enc` and` plain1.txt` are equal in size, so it's probably an XOR. I used the `xor.py` to extract the xored file and use it as the key to decrypt the flag.

```
$ xxd crypt1.enc 
00000000: 3c0d 0805 590a 1c41 1911 4512 1714 1303  <...Y..A..E.....
00000010: 0458 4811 0913 0b06 4f00 060d 450c 1717  .XH.....O...E...
00000020: 1a4f 1215 0515 0d13 0a43 0308 1f0d 4515  .O.......C....E.
00000030: 1e10 104f 0e1a 0d45 0303 0d43 1b09 1d1b  ...O...E...C....
00000040: 450e 181c 4306 1254 050c 0f13 5743 2218  E...C..T....WC".
00000050: 541b 040c 0615 064f 0807 4808 1856 1b06  T......O..H..V..
00000060: 1c15 540e 1708 1317 0743 411d 1c45 0805  ..T......CA..E..
00000070: 590e 1641 1801 0304 5859 4326 4119 1d16  Y..A....XYC&A...
00000080: 1556 1402 1c15 111a 4508 0255 430e 1254  .V......E..UC..T
00000090: 2145 0c03 0a17 4f0c 151b 1104 0459 0e16  !E....O......Y..
000000a0: 4118 0103 0458 5943 3808 0000 0a14 0259  A....XYC8......Y
000000b0: 0e0a 4119 1145 1217 1413 0304 5401 1641  ..A..E......T..A
000000c0: 030a 0603 0407 1b49 4101 1017 070e 011c  .......IA.......
000000d0: 450c 0f59 100e 0c04 0400 413f 5902 0241  E..Y......A?Y..A
000000e0: 011b 000d 130a 1041 41                   .......AA

$ xxd plain1.txt
00000000: 5468 6973 2069 7320 6d79 2073 616d 706c  This is my sampl
00000010: 652c 2074 6865 7265 2061 7265 206d 616e  e, there are man
00000020: 7920 7361 6d70 6c65 7320 6c69 6b65 2074  y samples like t
00000030: 6869 7320 6f6e 6520 6275 7420 7468 6973  his one but this
00000040: 206f 6e65 2069 7320 6d69 6e65 2e20 4d79   one is mine. My
00000050: 2073 616d 706c 6520 6973 206d 7920 6265   sample is my be
00000060: 7374 2066 7269 656e 642c 2069 7420 6973  st friend, it is
00000070: 206d 7920 6c69 6665 2e20 2049 206d 7573   my life.  I mus
00000080: 7420 6d61 7374 6572 2069 742c 2061 7320  t master it, as 
00000090: 4920 6d75 7374 206d 6173 7465 7220 6d79  I must master my
000000a0: 206c 6966 652e 2020 5769 7468 6f75 7420   life.  Without 
000000b0: 6d65 206d 7920 7361 6d70 6c65 2069 7320  me my sample is 
000000c0: 7573 656c 6573 732c 2077 6974 686f 7574  useless, without
000000d0: 206d 7920 7361 6d70 6c65 2049 2061 6d20   my sample I am 
000000e0: 7573 656c 6573 732e 20                   useless.

$ python xor.py crypt1.enc plain1.txt secret.key
[*] crypt1.enc XOR plain1.txt
[*] Saved to secret.key.

# The secret seems to be "heavycoat" :)
$ cat secret.key 
heavycoatheavycoatheavycoatheavycoatheavycoatheavycoatheavycoatheavycoatheavycoatheavycoatheavycoatheavycoatheavycoatheavycoatheavycoatheavycoatheavycoatheavycoatheavycoatheavycoatheavycoatheavycoatheavycoatheavycoatheavycoatheavycoa

$ python xor.py sample.enc secret.key flag.txt
[*] sample.enc XOR secret.key
[*] Saved to flag.txt.

$ cat flag.txt 
Flag:  Full_Xor'd_Jacket_Private
```

Flag is `Full_Xor'd_Jacket_Private!`
