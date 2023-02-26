P = float(input("Enter the present value of your account:"))
i = float(input("Enter your accounts monthly interest rate:"))
t = float(input("Enter the number of months that the money will be left in your account:"))


F = P*((1 + i)**t)
print("The information for your account is:\n Present Value:${0:.2f}\n Interest Rate:%{1:.2f}\n After {2:.2f} months the value of your account will be ${3:.2f}".format(P,i, t, F))



