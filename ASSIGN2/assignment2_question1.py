import random
x = random.randint(12,36)
y = random.randint(12,36)
z = random.randint(12,36)
print("x= ", x)
print("y= ", y)
print("z= ", z)



A=x+6==3+y
B=2*6-4>=9-z
C=6//y<3-1
D=18//x==2*3
E=not(x-y>=1)
F=z<=7 or y<12
G=(x+y!=40)and(x!=z)
H=(z-x>=y)or(y-x!=z+4)
I=(5-x<=2*y)and(y-15>=z)or(x-5!=y-2*z)
J=(True and False) or not(False or False)

print("A:x+6==3+y ->",A)
print("B:2*6-4>=9-z ->",B)
print("C:6//y<3-1 ->",C)
print("D:18//x==2*3 ->",D)
print("E:not(x-y>=1) ->",E)
print("F:z<=7 or y<12 ->",F)
print("G:(x+y!=40)and(x!=z) ->",G)
print("H:(z-x>=y)or(y-x!=z+4) ->",H)
print("I:(5-x<=2*y)and(y-15>=z)or(x-5!=y-2*z) ->",I)
print("J:(True and False) or not(False or False) ->",J)



