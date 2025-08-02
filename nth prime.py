# nth prime number

def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def nthprime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if prime(num):
            count += 1
    return num

n = int(input("Enter n to find the nth prime number: "))
print(f"The {n}th prime number is: {nthprime(n)}")
