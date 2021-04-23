#!/usr/bin/env python
"""
SANS_France_CTF_2021

Copyright (C) 2021  Nicolas Beguier

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Written by Nicolas BEGUIER (nicolas_beguier@hotmail.com)
"""

# Standard library imports
import base64
import sys
import zipfile

# Third-Party imports
from tqdm import tqdm

# The password list path you want to use, must be available in the current directory
WORDLIST = 'dict.txt'

# The zip file you want to crack its password
ZIP_FILE = 'c1000.zip'

# Initialize the Zip File object
ZIP_FILE = zipfile.ZipFile(ZIP_FILE)
# Count the number of words in this WORDLIST
n_words = len(list(open(WORDLIST, 'rb')))
# Print the total number of passwords
print('Total passwords to test:', n_words)

with open(WORDLIST, 'rb') as WORDLIST:
    for word in tqdm(WORDLIST, total=n_words, unit='word'):
        b64word = base64.b64encode(word.decode().split('\n')[0].encode())+b'\n'
        try:
            ZIP_FILE.extractall(pwd=b64word.strip())
        except:
            continue
        else:
            print('[+] Password found:', b64word.decode().strip())
            sys.exit(0)
print('[!] Password not found, try other wordlist...')
