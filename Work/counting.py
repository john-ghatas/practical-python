#!/bin/python
prices = {
        'GOOG' : 490.1,
        'AA' : 23.45,
        'IBM' : 91.1,
        'MSFT' : 34.23
    }

print(list(zip(prices.values(), prices.keys())))
