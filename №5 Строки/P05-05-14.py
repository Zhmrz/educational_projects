print("Пирамидка из букв")
S="Я_помню_чудное_мгновенье"
i=1
while (i<13):
    C=S[12-i:12+i]
    print(C.center(30, "_"))
    i+=1
#Второй способ
"""

while (i<13):
    C="{:_^30}".format(S[12-i:12+i])
    print(C)
    i+=1

"""
