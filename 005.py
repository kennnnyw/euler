# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

divisors = [11,12,13,14,16,17,18,19,20]
def isDivisible(num):
    for i in divisors:
        if num % i != 0:
            return False
    return True

num = 20
found = False
while found == False:
    if isDivisible(num):
        found = True
    num += 20

print(num)
