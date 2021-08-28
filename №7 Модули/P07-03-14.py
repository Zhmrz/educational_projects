from MathRand import *
numbers=""
summa=0
for i in range(10):
    x=RND(-10,20)
    summa+=x
    if i==9:
        numbers+=str(x)
        break
    numbers+=str(x)+", "
print(f"Последовательность из 10 целых чисел: {numbers}")
print(f"Сумма равна - {summa}")
print("Среднее арифметическое -",summa/10)
