def Sum(X,Y):
    summa=X+Y
    return summa

def Pif(a,b):
    c=(a**2)+(b**2)
    return c

def Garm(n):
    summa=0
    for i in range(1,n+1):
        summa+=1/i
    return summa

def Summ(M):
    summa=0
    for i in range(1,M+1):
        summa+=i
    return summa

def Average(M):
    sum=Summ(M)/M
    return sum

def Digits(n):
    l=len(str(n)) #длина строки=кол-во цифр
    summa=0
    for i in range(l):
        summa+=n % (10**(i+1)) // (10**i) #целочисленное деление и деление с остатком
        #summa+=int(str(n)[i]) # 2-й способ, срезаем каждое число и суммируем
    return summa

    """
    алгоритм деления (для цикла)
    123  % 10    //   1     = 3
    123  % 100   //   10    = 2
    123  % 1000  //   100   = 1

    1234 % 10    //   1     = 4
    1234 % 100   //   10    = 3
    1234 % 1000  //   100   = 2
    1234 % 10000 //   1000  = 1
    """
    
