#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random
import argparse

english_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

class Cipher():

	def __init__(self, key=None, proc=None, plainText=None, cipherText=None):
		self.key = key
		self.proc = proc
		self.reverse = False

	def keyInit(self):
		key = random.randint(2,len(english_alphabet)-1) # Rot-2 ve Rot-25 arasında bir şifreleme yapma imkanı
		self.key = key

	@staticmethod
	def charProc(text, key, proc, reverse):
		ret_text = ''
		for character in text.upper():
			index = english_alphabet.index(character)
			
			if reverse == True: # Reverse processing. Don't summary.
				if proc == 'e':
					index -= key
				else:
					index += key
			else:
				if proc == 'e':
					index += key
				else:
					index -= key

			index = index % len(english_alphabet)
			ret_text += english_alphabet[index]
		return ret_text

	def encrypt(self):
		print('-Key :',self.key)
		print('-Plain text:',self.plainText)

		print ('[+]\tEncryption is starting with ROT-',self.key)

		self.cipherText = self.charProc(self.plainText, self.key, self.proc, self.reverse)
		
		print ('[+]\tEncryption ended with ROT-',self.key)
		return self.cipherText

	def decrypt(self):
		print ('-Key :',self.key)
		print ('-Cipher text:',self.cipherText)

		print ('[+]\tDecryption is starting with ROT-',self.key)

		self.plainText = self.charProc(self.cipherText, self.key, self.proc)

		print ('[+]\tDecryption ended with ROT-',self.key)
		return self.plainText

	def bruteforce(self):
		print ('Brute force attack is starting.')
		print ('Cipher text:',self.cipherText)

		for i in range(0,len(english_alphabet)+1):
			self.plainText = self.charProc(self.cipherText, i, self.proc, True)
			print (self.plainText,'[ROT-',i,']')
			
			# Reverse bruteforce.
			#self.plainText = self.charProc(self.cipherText, i, self.proc, False)
			#print (self.plainText,'[ROT-',i,'] [Reverse]')

	def frequencyAnalysis(self):
		characters = {}
		characters[self.cipherText[0]] = 1

		for character in self.cipherText[1:]:
			if character:
				if character in characters.keys(): # if character in dictionary
					characters[character] += 1
				else:
					characters[character] = 1

		for i in english_alphabet:
			i = i.lower()
			if i in characters.keys():
				print ('%s : %d' %(i, characters[i]))



#############################################################################################


if __name__ == '__main__':
	
	caesar = Cipher()

	parser = argparse.ArgumentParser()
	parser.add_argument('-k','--key', help='Specify a key', type=int)
	parser.add_argument('-g','--generate', help='Generate a key', action='store_true')
	parser.add_argument('-e','--encrypt', help='Encrypt given plain text')
	parser.add_argument('-d','--decrypt', help='Decrypt given cipher text')
	parser.add_argument('-r','--reverse', help="Don't go forward-backward in encryption-decryption", action="store_true")
	parser.add_argument('-b','--breakcipher', help='Break given cipher text without key')
	parser.add_argument('-f','--frequency', help='Do Frequency analysis given cipher text')
	args = parser.parse_args()

	if not args.key and not args.generate and not args.breakcipher and not args.frequency:
		print("If you have a key. You must give with -k. If you haven't, you can generate a random key with -g.")
		exit(0)

	if args.key:
		caesar.key = args.key
	elif args.generate:
		caesar.keyInit()

	if args.reverse:
		caesar.reverse = True

	if args.encrypt:
		caesar.proc = 'e'
		caesar.plainText = args.encrypt
		caesar.encrypt()
		print (caesar.cipherText)

	elif args.decrypt:
		caesar.proc = 'd'
		caesar.cipherText = args.decrypt
		caesar.decrypt()
		print (caesar.plainText)

	elif args.breakcipher:
		caesar.proc = 'd'
		caesar.cipherText = args.breakcipher
		caesar.bruteforce() #brute force attack for all possible.

	elif args.frequency:
		caesar.cipherText = args.frequency
		caesar.frequencyAnalysis()
	
	else:
		print("Please give plain/cipher text")