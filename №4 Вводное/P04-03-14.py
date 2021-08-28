print("Таблица Пифагора")
for i in range(1,11):
    for p in range(1,11):
        if (i*p<10):
            print("  ",end="")
        if (i*p>9):
            print(" ",end="")
        print(i*p,end="")
    print()
