print("Четное-нечетное")
def ChN(N):
    x=0
    y=0
    z=""
    for i in range(2,N+1,2):
        x+=i-1  #нечетное
        a=str(i-1)+" -> "+str((i-1)*3)
        z+=a+"\n"
        y+=i    #четное
        b=str(i)+" -> "+str(i/2)
        z+=b+"\n"
    return z
w=ChN(10)
print(w)
