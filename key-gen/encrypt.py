#!/usr/bin/python3

import sys, base58

key = sys.stdin.readline()

decode = base58.b58decode(key.strip())

print(decode)
