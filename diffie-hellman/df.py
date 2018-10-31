#!/usr/bin/python3

import random as r

def generateAKey(a, n,g):
    # Generate the A key with the supplied values.
    aKey = (g ** a) % n
    # Return the A key.
    return aKey

def generateBKey(b, n,g):
    # Generate the B key.
    bKey = (g ** b) % n
    # Return the B key.
    return bKey

def findSharedSecret(pubKey, privKey, n,g):
    # Find the shared secret using n and g.
    shared = (pubKey ** privKey) % n
    # Return the shared key.
    return shared

def main():
    n = 797797
    g = 77
    r.seed(a=1)
    # Now generate Alice and Bob's keys.
    print("Generating Alice's key.")
    a = r.randint(0, n)
    alice = generateAKey(a,n,g)
    print("Generating Bob's key.")
    b = r.randint(0,n)
    bob = generateAKey(b,n,g)
    
    print("Finding shared secrets.")
    # Find the shared secrets.
    shared1 = findSharedSecret(alice, b, n, g)
    shared2 = findSharedSecret(bob, a, n, g)

    print("Alice shared secret {}".format(hex(shared1)))
    print("Bob shared secret {}".format(hex(shared2)))

if __name__ == "__main__":
    main()
