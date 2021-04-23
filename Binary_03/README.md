# Binary 03

There's a zip file we need to get into at https://xxxxxx/bh01.zip. All efforts so far have failed but maybe we're not trying hard enough. We do know that the password is base64 encoded however. Can you extract the file?

## Prerequisites

```
pip install -r requirements.txt
```

## Solution

To brute force a zip file with an encoded password, I used a common SecList (the xato one) and encoded each password in base64 with my `brute_force_zipfile.py` script to decrypt the zip file.

```
$ ls
brute_force_zipfile.py  c1000.zip  dict.txt

$ python brute_force_zipfile.py
Total passwords to test: 5189454
  0%|                                                                                                                                             | 0/5189454 [00:00<?, ?word/s][+] Password found: anVwaXRlcg==
  0%|                                                                                                                                 | 766/5189454 [00:00<09:33, 9041.94word/s]

$ unzip c1000.zip 
Archive:  c1000.zip
[c1000.zip] flag.txt password: 
 extracting: flag.txt                

$ cat flag.txt 
avoid_common_pws!
```

Flag is `avoid_common_pws!`
