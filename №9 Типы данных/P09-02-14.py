from random import *
print("Список из положительных элементов")
L1=[]
for i in range(10):
    L1.append(randint(-9,9))
print("L1=",L1)

L2=[]
for i in range(10):
    if L1[i]>=0:
        L2.append(L1[i])
print("L2=",L2)
