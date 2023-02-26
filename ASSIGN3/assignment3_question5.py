amnt = float(input("Enter a loan amount, for example 1200.78:"))
yr = int(input("Enter number of years as an integer, for example 5:"))
print()
print("Interest Rate   Monthly Payment   Total Payment")

for i in range(40,65,1):
    intrate = (i/8)/100
    num = (amnt * intrate)
    den = 1-(1/((1+intrate)**(yr*12)))
    mpay = num/den
    totpay = mpay * yr * 12
    print("{0:<16.3%}{1:<18.2f}{2:<13.2f}".format(intrate,mpay,totpay))


