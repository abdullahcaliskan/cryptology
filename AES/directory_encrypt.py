#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import socket
from Crypto.Cipher import AES
from Crypto import Random


class FileCipher():

    def __init__(self, anahtar, vektor):
        self.key = anahtar
        self.vektor = vektor
        self.plainText = ''
        self.cipherText = ''

    """def KeyTransfer(self, rhost, rport):
        cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cli_sock.connect( (rhost, rport) )

        byte_array = bytearray()
        byte_array.append(self.key)
        byte_array.append(self.vektor)

        cli_sock.send('K> '+byte_array[0])
        cli_sock.send('V> '+byte_array[1])

        cli_sock.shutdown(socket.SHUT_WR)
        cli_sock.close()"""

    def sifrele(self, duz_metin):
        self.plainText = duz_metin
        cipher = AES.new(self.key, AES.MODE_CFB, IV=self.vektor)
        sifreli_metin = cipher.encrypt(duz_metin)
        self.cipherText = sifreli_metin

    def sifreCoz(self, sifreli_metin):
        self.cipherText = sifreli_metin
        decryptor = AES.new(self.key, AES.MODE_CFB, IV=self.vektor)
        duz_metin = decryptor.decrypt(sifreli_metin)
        self.plainText = duz_metin

param = sys.argv[1]
device = sys.argv[2]
#rhost = sys.argv[3]
#rport = int(sys.argv[4])
"""anahtar = sys.argv[3]
vektor = sys.argv[4]

if not anahtar:
    pass
    # Bu kısımda random anahtar üretimi
if not vektor:
    pass
    # Bu kısımda 16 lık vektör üretimi random
"""
anahtar = b'abdullahcaliskan' # 16 bytelik key.
#vektor = Random.new().read(AES.block_size)
vektor = 16 * '\x00'
# Anahtar şimdilik, bu şekilde açık kalsın. Socket aktarımı yaparken
# RSA ile gönderimde bulunacam. Ayrıca Parola koruması getirecem.



dosyalar = []
for root, dirs, files in os.walk(device, topdown=True):
    for name in files:
        full_path = os.path.join(root, name)
        dosyalar.append(full_path)
        print(full_path)

cevap = input('Yukarıdaki dosyalar işlem görecek, emin misiniz? E/h\n>>> ')

if cevap.upper() == 'E':
    Sifreleyici = FileCipher(anahtar, vektor)
    #Sifreleyici.KeyTransfer(rhost, rport)
    for dosya_adi in dosyalar:
        fp = open(dosya_adi, "rb+")
        icerik = fp.read()
        if param == 'e':
            Sifreleyici.sifrele(icerik)
            print ('Şifrelendi - {}'.format(dosya_adi))
            fp_cipher = open(dosya_adi+'.enc', 'wb+')
            fp_cipher.write(Sifreleyici.cipherText)
        elif param == 'd':
            Sifreleyici.sifreCoz(icerik)
            print ('Şifre çözüldü - {}'.format(dosya_adi))
            fp_plain = open(dosya_adi+'.dec', 'wb+')
            fp_plain.write(Sifreleyici.plainText)

else:
    exit(0)
