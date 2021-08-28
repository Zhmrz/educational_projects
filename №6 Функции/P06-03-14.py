print("Среднее арифметическое")
def Avr(*x):
    summa=0
    for i in range(len(x)):
        summa=summa+x[i]
    avr=summa/len(x)
    return avr
w=Avr(1,2,3,4,5,6,7,8)
print(w)
