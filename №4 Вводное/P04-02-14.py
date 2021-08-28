print("Числа Фибоначчи")
x=1
y=1
for i in range(1,10):
    if (i==1) or (i==3) or (i==5) or (i==7) or (i==9):
        print(i,"->",x)
        x=x+y
    if (i==2) or (i==4) or (i==6) or (i==8):
        print(i,"->",y)
        y=y+x
