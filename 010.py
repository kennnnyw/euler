# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

def sumPrimes(n):
    # create a list containing n true values, where n is the biggest number
    # that we are checking (e.g. 2 million for this problem)
    # true means that the index position is a prime numbers
    # (starts off by assuming all number are prime, and then begins to
    # rule out numbers as primes are found)
    sieve = [True] * n
    sum = 0 # sum of the primes

    # can start the loop at 2 instead of 0, since 2 is the first prime number
    for i in range(2, n):
        if sieve[i] == True:
            sum += i # if the number if prime, then it is added to the sum
            # any multiples of a prime number is no longer prime, so can
            # set the corresponding positions in the list to false and they
            # will be ignored
            for j in range(2*i, n, i):
                sieve[j] = False
    return sum

print sumPrimes(2000000)
