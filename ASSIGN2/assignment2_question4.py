import random
ans=random.randint(0,1)
guess = int(input("Guess head or tail? Enter 0 for head and 1 for tail: "))
print(ans)
if ans != guess and ans==0:
    print("Sorry its a head")
elif ans != guess and ans==1:
    print("Sorry its a tail")
else:
    print("Correct Guess")


