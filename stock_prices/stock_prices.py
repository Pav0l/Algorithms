#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # keep track of lowest price, start at first price
    min = prices[0]
    # keep track of highest profit, start at first 2 prices
    profit = prices[1] - prices[0]

    # loop through the prices
    for i in prices:
        # compare current value with min
        if i < min:
            min = i
        # compare profit with current value vs previous profits
        # but make sure you are not calculating profit for the same value
        if i - min > profit and i != min:
            profit = i - min

    return profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
