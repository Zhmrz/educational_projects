print("Гармоническая сумма")
def G(N):
    G=0
    i=0
    while (G<N):
        i+=1    #Важно увеличивать счетчик в начале цикла
        x=1/i
        G+=x
    sum=f"Число слагаемых = {i}"
    return sum
A=int(input("A="))
y=G(A)
print(y)
