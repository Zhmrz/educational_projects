Name=input("Название продукта: ")
x=int(input("Макс.кол-во пачек: "))
price=float(input("Цена за пачку: "))
print(f'Список цен. Товар: "{Name}"')
print(" Кол   Цена   Стоимость")
i=1
while (i<x+1):
    y=i*price
    if i<10:
        print(f"  {i} x {price} = {y:0.2f}")
    else:
        print(f" {i} x {price} = {y:0.2f}")
    i+=1
