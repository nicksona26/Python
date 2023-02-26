sen = 0
negative = 0
positive = 0
acc = 0
count = 0

num = int(input("Enter an integer, the input ends if it is 0: "))

if num == 0:
    print("No numbers are entered except 0")

while num != sen:
    if num > 0:
        positive += 1
        acc += num
    else:
        negative += 1
        acc += num
    count += 1
    num = int(input("Enter an integer, the input ends if it is 0: "))

if count > 0:
    print("The number of positives is ",positive)
    print("The number of negatives is ",negative)
    print("The total is",acc)
    avg = acc/count
    print("The average is {0:.2f}".format(avg))
