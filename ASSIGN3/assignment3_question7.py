import random
count = 1
while count < 6:
    x = random.randint(100,999)
    p1 = x % 10
    y = x // 10
    p2 = y % 10
    y2 = y // 10
    p3 = y2 % 10
    if (p1 == p2) and (p2 == p3):
        print("Lottery number",count,":",x)
        count += 1
