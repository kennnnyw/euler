# A Pythagorean triplet is a set of three natural numbers,
# a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def pythagTriplet():
    for a in range(1, 1000):
        for b in range(a+1, 1000): # a+1 since b must always be greater than a
            c = 1000 - b - a
            if (a*a) + (b*b) == (c*c):
                print ("a: " + str(a))
                print ("b: " + str(b))
                print ("c: " + str(c))
                print ("a * b * c = " + str(a*b*c))

print (pythagTriplet())
