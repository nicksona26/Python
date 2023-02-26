def encrypt(f1,f2):
    file = open(f1,'r')
    lines = []
    encLines = []
    for line in file:
        lines.append(line)
    file.close()
    for line in lines:
        evenCh = ""
        oddCh = ""
        count = 0
        for ch in line:
            if count % 2 == 0:
                evenCh += ch
            else:
                oddCh += ch
            count += 1
        cipherText = oddCh + evenCh
        encLines.append(cipherText)
    file = open(f2,'w')
    for line in encLines:
        file.write(line)
    file.close()        
    
def decrypt(f1,f2):
    file = open(f1,'r')
    encLines = []
    decLines = []
    for line in file:
        encLines.append(line)
    file.close()
    for line in encLines:
        halfLength = len(line)//2
        oddChars = line[:halfLength]
        evenChars = line[halfLength:]
        decLine = ''
        for i in range(halfLength):
            decLine +=  evenChars[i]
            decLine += oddChars[i]
        if len(oddChars)<len(evenChars):
            decLine += evenChars[-1]
        decLines.append(decLine)
    file = open(f2,'w')
    for decLine in decLines:
        file.write(decLine)
    file.close()        
    
def main():
    f1 = input("Enter a source filename: ")
    f2 = input("Enter a target filename: ")
    choice = input("Enter E to encrypt or D to decrypt the input file: ")
    if choice == 'E':
        encrypt(f1,f2)
    elif choice == 'D':
        decrypt(f1,f2)

main()
