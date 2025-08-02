# Fibonacci series up to n terms
def fibo_series(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter the number of terms: "))
print("Fibonacci series:")
fibo_series(n)
