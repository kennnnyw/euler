# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def findLPF(n):
    factors = []
    i = 2
    while i < n:
        if n % i == 0:
            n = n / i
            factors.append(i)
        i += 1;
    factors.append(n)
    return max(factors)

print (findLPF(600851475143))

# still contains some bugs... 
