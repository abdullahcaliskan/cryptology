#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random
import math
import time
import binascii

class RandomAsal():
    def __init__(self):
        self.deger = 0
        self.durum = 1

    def sayiUret(self):
        #self.deger = random.randint(3, 999999999999999999999999) # 24 basamaklı olsun.
        #self.deger = random.randint(3, 999999999) # 9 basamaklı olsun.
        self.deger = random.randint(3, 9999999999999999) # 16 basamaklı olsun.
        self.durum = 1
        karekokDeger = math.ceil(self.deger ** 0.5) + 1

        if self.deger % 2 == 0 : # Sayı 2'ye bölünebiliyorsa, Asal Değildir.
            self.durum = 0 # 0 demek : Asal degil demek. işlem başarısız.
            return 0
        for i in range(3, karekokDeger, 2):
            if self.deger % i == 0: # Sayı i değerlerinden birisine bölünebiliyorsa, Asal Değildir.
                self.durum = 0 # Asal degil demek.
                break # işlem yapmaya gerek yok.

############# P Degeri ####################             INIT
# P degerini üretiyorum.
start_time = time.time()
p = RandomAsal()
p.sayiUret()
deneme = 1
# Sayı asal degilse, tekrar üretiyorum.
while p.durum != 1:
    p.sayiUret()
    deneme += 1
print('p : ',p.durum, deneme, p.deger)
############## Q Degeri ###################             INIT
# Q degerini üretiyorum.
q = RandomAsal()
q.sayiUret()
deneme = 1
while q.durum == 0 and q.deger != p.deger:
    q.sayiUret()
    deneme += 1
print('q : ',q.durum, deneme, q.deger)

##############################################################

# p ve q degerleri büyük ve asal olmalılar..
n = p.deger * q.deger
# Phi_n degeri formülü >> (p-1) * (q-1)
Phi_n = n - p.deger - q.deger + 1

# e degerini sabit olarak alıyoruz. 2^16 + 1 olması gerek. burda Kare Al ve çarp işlemini yapacağız. pubkey
e = 65537

# d : privkey degeri.
d = ( (2 ** 16)+1 ) ** -1   # e ^ -1
d = d % Phi_n
end_time = time.time()
#print ('n : ', n)
#print (hex(n))
#print (':'.join('{:65x}'.format(ord(c)) for c in n))

fp = open('test.n', 'w')
#hs = str(n)
#hb = binascii.a2b_hex(hs)

hexa = "{0:x}".format(n).upper()
fp.write(hexa)

fp.close()

print ('Phi_n : ', Phi_n)
print ('d : ', d)
print ('e : ', e)
print ('{} saniyede oluşturuldu.'.format(end_time-start_time))

plainText = 'abdullah'
plainText = ' '.join(format(ord(x), 'b') for x in plainText)

cipherText = ( plainText ** ((2 ** 16)+1) ) % n


print(cipherText)