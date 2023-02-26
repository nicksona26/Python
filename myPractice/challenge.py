import random
def doors():
  print (''' 
_____1_____    _____2____   _____3_____
|  __  __  |  |  __  __  |  |  __  __  |
| |  ||  | |  | |  ||  | |  | |  ||  | |
| |  ||  | |  | |  ||  | |  | |  ||  | |
| |__||__| |  | |__||__| |  | |__||__| |
|  __  __()|  |  __  __()|  |  __  __()|
| |  ||  | |  | |  ||  | |  | |  ||  | |
| |  ||  | |  | |  ||  | |  | |  ||  | |
| |  ||  | |  | |  ||  | |  | |  ||  | |
| |  ||  | |  | |  ||  | |  | |  ||  | |
| |__||__| |  | |__||__| |  | |__||__| |
|__________|  |__________|  |__________|''')

def monster():
    print ('''
        .-""-"-""-.
       | .--.-.--. |
       |` >       `|
       | <         |
       (__..---..__)
      (`|\o_/ \_o/|`)
       \(    >    )/
     [>=|   vvv   |=<]
        \__\   /__/
            '-'
 ''')
print ('Halloween Game')
print ('Avoid the monster!')
monsterdoor = random.randint(1,3)
fail = 0
win = 0
restart = "Y"
while restart != "N":
    doors()
    choice = int(input("Pick a door: "))
    if choice < 1 or choice > 3:
        choice = input("Only 3 doors pick again: ")
    if choice == monsterdoor:
        monster()
        print("AHHHHHHHHHHHHH")
        fail+=1
        restart=input("Restart? Y for yes, N for no: ")
    else:
        win+=1
        print("whew.. close one")
        restart=input("Restart? Y for yes, N for no: ")
print("You got caught by the monster ",fail," times")
print("You got away ",win," times")
