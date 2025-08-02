

# Count the prime numbers

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

start = 1
end = 50
count = 0
primes = []  # Initialize the list to store prime numbers

for n in range(start, end + 1):
    if prime(n):
        primes.append(n)
        count += 1

print("Number of prime numbers between", start, "and", end, "is:", count)
print(primes)
