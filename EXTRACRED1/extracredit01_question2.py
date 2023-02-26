alphabet = "abcdefghijklmnopqrstuvwxyz "
testKey = "zyxwvutsrqponmlkjihgfedcba "

def encrypt(plainText,key):
    plainText = plainText.lower()
    cipherText = ""
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText += key[idx]
    return cipherText


def decrypt(cipherText,key):
    plainText = ""
    for ch in cipherText:
        idx = testKey.find(ch)
        plainText += alphabet[idx]
    return plainText

def main():
    msg = input("Enter a message ")
    cipherText = encrypt(msg,testKey)
    print("CipherText:",cipherText)
    print("PlainText:",decrypt(cipherText,testKey))

main()
