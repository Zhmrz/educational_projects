def Write(Mess):
    print(Mess,end="")

def WriteLn(Mess):
    print(Mess)

def ReadStr(Mess):
    while True:
        l=input(f"{Mess}")
        if l.isalpha()==True:
            break
    return l
        
def ReadInt(Mess):
    while True:
        x=input(f"{Mess}")
        if x.isdigit()==True and str(x).find(".")==-1:
            break

def ReadFloat(Mess):
    while True:
        x=input(f"{Mess}")
        if x.isalpha()==False and str(x).find(".")>0:
            break
