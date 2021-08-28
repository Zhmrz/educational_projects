S="Лесенка"
print(S)
for i in range(1,6):
    A=S[:i]
    B="_"
    C=S[i+1:]
    print(A+B+C)
