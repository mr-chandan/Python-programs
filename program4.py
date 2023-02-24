# write a iterative and an recursive program to produce fibonacci series for given number


def fibonacci_iterative(n):
    fib_series = []
    a = 0
    b = 1
    while a <= n:
        fib_series.append(a)
        c = a + b
        a = b
        b = c
    return fib_series



def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


n = int(input("Enter a number: "))
print("Fibonacci series using iterative approach:", fibonacci_iterative(n))
print("Fibonacci series using recursive approach:")
for i in range(n+1):
    print(fibonacci_recursive(i))
