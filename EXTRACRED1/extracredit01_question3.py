alphabet = "abcdefghijklmnopqrstuvwxyz"

def rot13(msg):
    msg = msg.lower()
    cipherText = ""
    for ch in msg:
        idx = alphabet.find(ch)
        if idx + 13 > 25:
            cipherText += alphabet[idx + 13 - 26]
        else:
            cipherText += alphabet[idx + 13]
    return cipherText


def main():
    msg = input("Enter text message ")
    cipherText = rot13(msg)
    print("After encrypting",msg,"the cipherText message is",cipherText)
    print("After decrypting",cipherText,"the plainText message is",rot13(cipherText))

main()
