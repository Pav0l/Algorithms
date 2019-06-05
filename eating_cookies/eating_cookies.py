#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

# cache={"0": 0, "1": 1, "2": 2, "3": 4}


def eating_cookies(n, cache=None):
    # base conditions:
    if n <= 0:
        return 1
    # 1 cookie can be eaten only 1 way
    elif n == 1:
        return 1
    # 2 cookies can be eaten 2 ways (1+1 or 2)
    elif n == 2:
        return 2
    # 3 cookies can be eaten 4 ways (1+1+1 or 2+1 or 1+2 or 3)
    elif n == 3:
        return 4
    else:
        # do recursion for every Cookie Monster capability
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
