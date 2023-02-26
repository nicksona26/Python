def menu():
    print()
    print("Menu")
    print("---------------------------------------")
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5. Quit the program")
    print()

def load(f):
    emailDict = {}
    file = open(f,'r')
    for line in file:
        l = line.split()
        pair = []
        for word in l:
            pair.append(word)
        if pair != []:
            emailDict[pair[0]] = pair[1]
    return emailDict
    file.close()

def save(emailDict):
    file = open("EmailAdresses.txt", 'w')
    file.close()
    file = open("EmailAdresses.txt", 'a')
    names = list(emailDict.keys())
    emails = list(emailDict.values())
    for i in range(0,len(names)):
        file.write(names[i])
        file.write(' ')
        file.write(emails[i]+'\n')
    file.close()

def lookup(emailDict):
    name = input("Enter a name: ")
    if name not in emailDict:
        print("The specified name was not found")
    else:
        email = emailDict[name]
        print("Email:",email)
    
def delete(emailDict):
    name = input("Enter name: ")
    if name not in emailDict:
        print("The specified name was not found")
    else:
        del emailDict[name]
        print("Information deleted")

def change(emailDict):
    name = input("Enter name: ")
    if name not in emailDict:
        print("The specified name was not found")
    else:
        email = input("Enter the new address: ")
        emailDict[name] = email
        print("Information updated")

def add(emailDict):
    name = input("Enter name: ")
    email = input("Enter email address: ")
    if name in emailDict:
        print("That name already exists")
    else:
        emailDict[name] = email
        print("Name and address have been added")
    
def main():
    choice = 0
    emailDict = load("EmailAdresses.txt")
    while choice != 5:
        menu()
        choice = int(input("Enter your choice: "))
        while choice > 5 and choice < 1:
            print("Number chosen is not an option. Try again.")
            choice = int(input("Enter your choice: "))
        if choice == 5:
            save(emailDict)
            print("Information saved")
            continue
        elif choice == 4:
            delete(emailDict)
        elif choice == 3:
            change(emailDict)
        elif choice == 2:
            add(emailDict)
        elif choice == 1:
            lookup(emailDict)
         
main()




