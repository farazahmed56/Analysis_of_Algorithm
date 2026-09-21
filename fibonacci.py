def Fib(n):
    if n < 2:
        return 1
    else:
        return Fib(n-1)+ Fib(n-2)

n = int(input("Enter number: "))
print(f"Fib({n}) = {Fib(n)}")