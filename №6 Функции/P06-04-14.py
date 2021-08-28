print("Среднее гармоническое")
def AvrG(*x):
    q=0
    for i in range(len(x)):
        q=q+1/x[i]
    avr=len(x)/q
    return avr
w=AvrG(1,2,3,4,5,6,7,8)
print(w)
