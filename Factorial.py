def Fact(n):
    if n == 0:
        return 1
    else:
        return n * Fact(n-1)

print(Fact(5))