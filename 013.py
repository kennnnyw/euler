# Work out the first ten digits of the sum of the following
# one-hundred 50-digit numbers.

file = open("013.txt","r")
numbers = file.readlines()
file.close()

for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])

print str(sum(numbers))[0:10]
