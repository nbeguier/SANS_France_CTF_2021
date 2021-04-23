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
import itertools

def leet(word):
    """
    Return all variation of a string in l33t speak
    """
    leet_matches = [['a', '4', '@', 'A'],
    ['b' ,'8', 'B'],
    ['c'],
    ['d', 'D'],
    ['e', '3'],
    ['f'],
    ['g', '6'],
    ['h'],
    ['i', '1'],
    ['j'],
    ['k'],
    ['l'],
    ['m'],
    ['n'],
    ['o', '0', 'O'],
    ['p', 'P'],
    ['q'],
    ['r', 'R'],
    ['s', '5', 'S', '$'],
    ['t', '7'],
    ['u'],
    ['v'],
    ['w', 'W'],
    ['x'],
    ['y'],
    ['z', '2']]
    l = []
    for letter in word:
        for match in leet_matches:
            if match[0] == letter:
                l.append(match)
    return list(itertools.product(*l))

combo = leet("password")

for c in combo:
    print(f'{"".join(c)}')
    print(f'{"".join(c)}!')
    print(f'{"".join(c)}2019')
    print(f'{"".join(c)}2020')
    print(f'{"".join(c)}2021')
    print(f'{"".join(c)}2019!')
    print(f'{"".join(c)}2020!')
    print(f'{"".join(c)}2021!')
