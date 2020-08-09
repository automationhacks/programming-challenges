import unittest

"""
Writing programming interview questions hasn't made me rich yet ... so I might give up and start trading
Apple stocks all day instead.

First, I wanna know how much money I could have made yesterday if I'd been trading Apple stocks all day.

So I grabbed Apple's stock prices from yesterday and put them in a list called stock_prices, where:

    The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
    The values are the price (in US dollars) of one share of Apple stock at that time.

So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase
and one sale of one share of Apple stock yesterday.

For example:

  stock_prices = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices)
# Returns 6 (buying for $5 and selling for $11)

No "shorting"—you need to buy before you can sell. Also, you can't buy and sell in the same time step—at least 1 minute has to pass
"""

"""
O(n) time and O(1) space. We only loop through the list once. 
 We’ll greedily walk through the list to track the max profit and lowest price so far.

For every price, we check if:

    we can get a better profit by buying at min_price and selling at the current_price
    we have a new min_price

To start, we initialize:

    min_price as the first price of the day
    max_profit as the first profit we could get

We decided to return a negative profit if the price decreases all day and we can't make any money. 
We could have raised an exception instead, but returning the negative profit is cleaner, makes our function 
less opinionated, and ensures we don't lose information. 
"""


def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    # We'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    # Start at the second (index 1) time
    # We can't sell at the first time, since we must buy first,
    # and we can't buy and sell at the same time!
    # If we started at index 0, we'd try to buy *and* sell at time 0.
    # This would give a profit of 0, which is a problem if our
    # max_profit is supposed to be *negative*--we'd return 0.
    for current_time in range(1, len(stock_prices)):
        current_price = stock_prices[current_time]

        # See what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # Update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # Update min_price so it's always
        # the lowest price we've seen so far
        min_price = min(min_price, current_price)

    return max_profit


class AppleStockTest(unittest.TestCase):
    def test_profit_when_lowest_price_comes_first(self):
        stock_prices = [10, 7, 5, 8, 11, 9]
        self.assertEqual(get_max_profit(stock_prices), 6)

    def test_profit_when_highest_price_comes_first(self):
        stock_prices = [20, 7, 5, 3, 11, 9]
        self.assertEqual(get_max_profit(stock_prices), 8)
