#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import rsa

def WriteFile(dosya_adi, icerik):
    file_pointer = open(dosya_adi, 'wb')
    file_pointer.write(icerik)
    file_pointer.close()

def ReadFile(dosya_adi):
    file_pointer = open(dosya_adi, 'rb')
    icerik = file_pointer.read()
    file_pointer.close()
    return icerik
if(os.path.isfile('id_rsa')):
    privkey = ReadFile('id_rsa')
    pubkey = ReadFile('id_rsa.pub')

else:
    (pubkey, privkey) = rsa.newkeys(2048)

    WriteFile('id_rsa', privkey)
    WriteFile('id_rsa.pub', pubkey)

param = sys.argv[1]
file = sys.argv[2]

fp = open(file, "rb+")
content = fp.read()

if param == 'e':
    cipherText = rsa.encrypt(content, pubkey)
    WriteFile(file+'.enc', cipherText)
    # pubkey ile şifreliyorum.
elif param == 'd':
    cipherText = ReadFile(file)
    plainText = rsa.decrypt(cipherText, privkey)
    WriteFile(file+'.dec', plainText)
    # privkey ile şifre çözüyorum
