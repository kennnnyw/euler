# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

power_num = 2 ** 1000

sum = 0
for i in range(0, len(str(power_num))):
    # treat power_num as a string and the select the char at position i
    # convert the digit back to a digit and add it to the sum
    sum += int(str(power_num)[i])

print sum
