print("Счастливый билет?")
N=input("N=")
def Sum(N):
    x=int(N[0])+int(N[1])+int(N[2])
    y=int(N[3])+int(N[4])+int(N[5])
    if (x==y):
        return "Счастливый"
    else:
        return "Несчастливый"
print(Sum(N))
