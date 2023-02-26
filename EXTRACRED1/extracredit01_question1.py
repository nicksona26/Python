def encode(plainText):
    r1 = ""
    r2 = ""
    r3 = ""
    for i in range(len(plainText)):
        if i % 3 == 0:
            r1 += plainText[i]
        elif (i-1) % 3 == 0:
            r2 += plainText[i]
        elif (i+1) % 3 == 0:
            r3 += plainText[i]
    cipherText = r3 + r2 + r1
    return cipherText

def main():
    plainText = input("Enter a message ")
    print("PlainText:",plainText)
    print("CipherText:",encode(plainText))

main()
