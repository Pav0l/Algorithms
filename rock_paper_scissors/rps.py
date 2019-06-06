#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # define a list with R-P-S options and
    # list to contain the results
    rps = ['rock', 'paper', 'scissors']
    res = []

    # helper funciton to pass number of round = m
    # and a list that contains results from previous rounds
    def helper(m, saved_arr):
        # end condition
        if m == 0:
            # if we're at 0 rounds, append list to the resulting list
            res.append(saved_arr)
            return

        # for every option in rps add the option to the list and run the fn again
        for i in rps:
            # run this function 3 times for every 'rock', 'paper', 'scissors' m number of times
            new_arr = saved_arr + [i]
            helper(m-1, new_arr)
    helper(n, [])
    return res


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
