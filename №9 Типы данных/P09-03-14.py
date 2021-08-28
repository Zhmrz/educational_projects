from random import *
print("Неповторяемость элементов")
L1=[]
for i in range(10):
    L1.append(randint(0,9))
print(L1)
for i in range(10):
    for p in range(10):
        if i==p:
            continue #чтобы не сравнивать элемент с самим собой
        if L1[i]==L1[p]:
            print("Есть одинаковые")
            X=True #признак для внешнего цикла (чтобы break-нуть внешний цикл)
            break
    if X==True:
        break
