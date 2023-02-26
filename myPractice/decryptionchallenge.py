import random, time

#A basic encryption algorithm...
def encrypt(plaintext, key):
  alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  ciphertext = ""
  for i in range(0,len(plaintext)):
    character = plaintext[i]
    ciphertext = ciphertext + character
    for j in range (0,key):
      ciphertext = ciphertext + random.choice(alphabet)
  return ciphertext

#Main program starts here...
#Input...
plaintext = input("Enter a message to encrypt (plaintext)")
key = int(input("Input a key as a number between 1 and 10"))
while not (key>=1 and key<=10):
  print("Invalid key, try again!")
  key = int(input("Input a key as a number between 1 and 10"))

#Process...  
print("...")
time.sleep(1)
print("Encrypting plaintext...")
time.sleep(1)
print("...")
time.sleep(1)
ciphertext = encrypt(plaintext, key)
    

#Output...
print("Ciphertext:")
print(ciphertext)

#decrypt
def decrypt(ciphertext,key):
    plaintext2 = ""
    for i in range(0,len(ciphertext),key+1):
        character = ciphertext[i]
        plaintext2 += character
    return plaintext2

#process
print("...")
time.sleep(1)
print("Decrypting plaintext...")
time.sleep(1)
print("...")
time.sleep(1)
plaintext2 = decrypt(ciphertext, key)

#output
print("decrypted message:")
print(plaintext2)
    
