#multiplication table

print("\tMultiplication Table")
print("   ",end=" ")
for i in range(1,10):
    print('{0:2d}'.format(i),end=" ")
print("\n-------------------------------")
for j in range(1,10):
    print(j,"|",end=" ")
    for i in range(1,10):
        print('{0:2d}'.format(j*i),end=" ")
    print()
