print("Числа Фибоначчи")
def Fib(n):
    x=1
    y=0
    a=1
    b=0
    for i in range(1,n+1):
        if Q(i)==True:
            x=x+y  #нечетное число
        if Q(i)==False:
            y=x+y  #четное число
    if Q(n)==True:
        return x
    if Q(n)==False:
        return y

#Функция, которая показывает четное число или нечетное
def Q(n):
    a=1
    b=0
    for i in range(1,n):
        a+=2
        if n==a:
            return True #если нечетное
    for i in range(1,n):
        b+=2
        if n==b:
            return False #если четное

n=int(input("n="))
y=Fib(n)
print(f"Fib ( {n} ) = {y}")
