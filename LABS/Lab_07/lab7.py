def countLetter(s,ch):
    charCount = 0 
    for char in s:
        if char == ch:
            charCount += 1
    return charCount
        
def main1():
    inp = input("Enter a string:")
    let = input("Enter a character:")
    print("The number of \'{0}\' in \"{1}\" is".format(let,inp),countLetter(inp,let))
    
main1()

def countDigits(s):
    digCount = 0
    for ch in s:
        if ch == str(0) or ch == str(1) or ch == str(2) or ch == str(3) or ch == str(4) or ch == str(5) or ch == str(6) or ch == str(7) or ch == str(8) or ch == str(9):
            digCount += 1
    return digCount

def main2():
    inp = input("Enter another string:")
    print("The number of digits in \"{0}\" is".format(inp),countDigits(inp))

main2() 
            
    
