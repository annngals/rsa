# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 19:25:25 2020

@author: Anna Galsanova
"""
from math import gcd
import base64


def compare(a, b):
    return gcd(a, b) == 1

def split(word): 
    return [s for s in word]

def prime(n):
    if (n <= 1) : 
        return False
    if (n <= 3) :
        return True
    if (n % 2 == 0 or n % 3 == 0) :
        return False
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True

def keys(p,q):
    if prime(p) and prime(q):
        n = p * q
        print("n = ", n)
        eller = (p - 1) * (q - 1)
        print("φ =", eller)
        e = 2
        while e < eller: 
            e+=1
            if compare(e, eller):
                buff = e
        e = buff
        print("e =", e)
        d = 0
        while ((d * e) % (eller)) != 1:
            d +=1
        print("d =", d)
    else:
        print("Not prime numbers. Rerun program and try again")
    pubkey = (e, n)
    privkey = (d, n)
    return pubkey, privkey

def encrypt_rsa(message, pub_key):
    e = pub_key[0]
    n = pub_key[1]
    encm = []
    for i in message:
        i = ord(i)
        encoded = (i ** e ) % n
        encm.append(encoded)
    return encm 

def decrypt_rsa(message, priv_key):
    d = privkey[0]
    n = privkey[1]
    decm = []
    for i in message:
        i = int(i)
        decoded = (i ** d ) % n
        decoded = chr(decoded)
        decm.append(decoded)
    return decm 

def encrypt_b(message):
    enc = []
    for i in message:
        dec = base64.b64encode(bytes(str(i), 'ascii'))
        enc.append(dec)
    return enc

def decrypt_b(message):
    enc = []
    for i in message:
        dec = base64.b64decode(i)
        enc.append(dec)
    return enc

p = int(input("Input prime integer: p = "))
q = int(input("Input second prime integer (a different one): q = "))

(pubkey, privkey) = keys(p, q)
delimiter = ""

message = 'Hello'
list_message = split(message)
crypto = encrypt_rsa(list_message, pubkey)
print("Encrypted message: ", delimiter.join([str(item) for item in crypto]))
encb = encrypt_b(crypto)
print("Encoded base64: ", delimiter.join([str(item) for item in encb]))
decb = decrypt_b(encb)
print("Decoded base64: ", delimiter.join([str(item) for item in decb]))
message = decrypt_rsa(decb, privkey)
print("Decrypted message: ", delimiter.join([str(item) for item in message]))