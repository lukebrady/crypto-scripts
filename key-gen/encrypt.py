#!/usr/bin/python3

import sys, base58, hashlib

# Decode the supplied key to encrypt the given message.
def decodeKey(key):
    decode = base58.b58decode(key.strip())
    intKey = int.from_bytes(decode, byteorder='big')
    return intKey

# Encrypt the supplied message with the supplied key.
def encryptMessage(message, key):
    msg = [(ord(char) * key) for char in message]
    msgHash = '8348483' #hashlib.sha256(bytes(msg)).hexdigest()
    # Return a tuple with the msg and msgHash.
    return (msg, msgHash)

# Get the key from stdin, decode the key, and encrypt
# the supplied message. Exit with code=1 if message
# is not supplied to the program.
def main():
    if len(sys.argv) < 2:
        sys.stdin.readline()
        print('A message was not supplied.')
        print('Exiting...')
        exit(code=1)
    else:
        key = sys.stdin.readline().strip()
        intKey = decodeKey(key)
        msg = encryptMessage(sys.argv[1], intKey)
        print('MSG: {}'.format(msg[0]))
        print('Hash: {}'.format(msg[1]))
        exit(code=0)

if __name__ == '__main__':
    main()
