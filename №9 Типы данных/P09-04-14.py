from random import *
print("Удаление элементов по условию")
L1=[]
for i in range(12):
    L1.append(randint(0,11))
print("L1=",L1)
L2=[a for a in L1 if a==3 or a==4 or a==5]
L1=[a for a in L1 if a!=3 and a!=4 and a!=5]
print("L1=",L1)
print("L2=",L2)
