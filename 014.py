# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

def get_chain_length(n):
    start = n
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
        seq.append(n)
    return len(seq)

def find_longest_chain(n):
    start_num = 13
    longest_chain_length = 10
    longest_start_num = start_num

    for i in range(start_num, n):
        current_length = get_chain_length(i)
        if current_length > longest_chain_length:
            longest_start_num = i
            longest_chain_length = current_length
    print "Start number: " + str(longest_start_num)
    print "Chain length: " + str(longest_chain_length)

find_longest_chain(1000000)
