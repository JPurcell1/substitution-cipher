import random
import copy

plaintext = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
encrypted = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
ciphertext = ""

def generate_key():
 """Generates an encrytpion key by uniquely pairing characters of the alphabet"""

 copy_of_plaintext = copy.deepcopy(plaintext) #copy of plaintext array in current form
 random.shuffle(copy_of_plaintext) #randomize the keyspace to create pairs for encryption
 encrypted = copy_of_plaintext

 print(f"plaintext= {plaintext}")
 print(f"encrypted= {encrypted}\n")

 return encrypted


def encrypt(key):
 """Transforms message to ciphertext using key sequence generated"""

 ciphertext = ""
 msg = input("Enter a string to encrypt (-1 to quit): ").lower()

 if msg != "-1":
   for letter in msg:
     if letter in plaintext: #if letter is in the keyspace
       index = plaintext.index(letter)
       ciphertext += key[index]
     else: #for spaces and other symbols not in keyspace
       ciphertext += letter
  
 print(f"\nYour encrypted message reads: {ciphertext}\n")
 return ciphertext


def decrypt(key, ciphertext):
 """Decodes ciphertext back into readable english"""

 decoded_msg = ""

 for letter in ciphertext:
   if letter in plaintext:
     index = key.index(letter)
     decoded_msg += plaintext[index]
   else:
     decoded_msg += letter

 print(f"The original message is: {decoded_msg}")


key = generate_key()
ciphertext = encrypt(key)
decrypt(key, ciphertext)