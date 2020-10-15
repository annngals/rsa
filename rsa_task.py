# -*- coding: utf-8 -*-
"""
@author: Anna Galsanova
"""
import rsa
import base64

(pubkey, privkey) = rsa.newkeys(512)

s = "hello"
message = s.encode('utf8')
crypto = rsa.encrypt(message, pubkey)
enc = base64.b64encode(crypto)
dec = base64.b64decode(enc)

print ("Input message: ", s)
print ("Encrypted message: ", crypto)
print ("Decrypted message: ", message)
print ("Decoded message:", message.decode('utf8'))
print ("Encoded base64: ", enc)
print ("Decoded base64: ", rsa.decrypt(dec, privkey).decode('utf8'), "\n")

print ("Public key: ", pubkey)
print ("Private key: ", privkey)
