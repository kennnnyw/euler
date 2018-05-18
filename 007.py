# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
#
# What is the 10,001st prime number?

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def nthPrime(n):
    primesFound = 0
    i = 1
    while primesFound != n:
        i += 1
        if isPrime(i) == True:
            primesFound += 1
    return i

print nthPrime(10001)



# works, but needs improvement (is very slow)
