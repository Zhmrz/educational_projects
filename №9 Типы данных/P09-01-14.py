print("Сумма чисел в конец списка")
L=list(a for a in range(10))
print(L)
summa=0
for i in L:
    summa+=L[i]
L.append(summa)
print(L)
