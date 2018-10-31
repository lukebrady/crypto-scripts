#!/usr/bin/python3

import random as r, base58, sys

def genKey(seed):
    r.seed(seed)
    # Generate a secure key based on the seed given.
    privKey = bytes([r.randint(0,255) for x in range(64)])
    # Now return the encoded private key string.
    return base58.b58encode(privKey).decode('utf-8')

def main():
    if len(sys.argv) < 2:
        key = genKey(92939)
        print(key)
    else:
        key = genKey(sys.argv[1])
        print(key)


if __name__ == '__main__':
    main()
