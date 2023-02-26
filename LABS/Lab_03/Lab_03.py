W = float(input("Enter the weight of the package: "))
N = float(input("Enter the number of packages: "))

if W > 10:
    print("Shipping charge for one package: $3.80")
    priceAll = 3.8 * N
    print("Shipping charge for all packages: ${0:.2f}".format(priceAll))
elif 6 < W <= 10:
    print("Shipping charge for one package: $3.70")
    priceAll = 3.7 * N
    print("Shipping charge for all packages: ${0:.2f}".format(priceAll))
elif 2 < W <= 6:
    print("Shipping charge for one package: $2.20")
    priceAll = 2.2 * N
    print("Shipping charge for all packages: ${0:.2f}".format(priceAll))
else:
    print("Shipping charge for one package: $1.10")
    priceAll = 1.1 * N
    print("Shipping charge for all packages: ${0:.2f}".format(priceAll))

if N > 5:
    discountPrice = priceAll - (priceAll * .05)
    print("Shipping charge for all packages after discount: ${0:.2f}".format(discountPrice))
else:
    print("Number of packages is less than 5; there is no discount")
    
