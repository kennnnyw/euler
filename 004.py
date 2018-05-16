# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def largestPalindrome(lower, upper):
    current = lower
    x = current
    y = lower
    largest = 0
    while x <= upper:
        result = x * y
        if result > largest:
            ans = str(result)
            if ans == ans [::-1]:
                largest = result

        if y == upper:
            current += 1
            x = current
            y = lower
        y += 1
    return largest

print (largestPalindrome(100,999))
