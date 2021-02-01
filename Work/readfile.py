#!/bin/python
import sys

def six_one(filename):
    try:
        with open(filename, 'rt') as file:
            headers = next(file).replace("\n","").split(",")
            shares = []
            for line in file:
                line = line.replace("\n","").split(",")
                index = 0
                share = {}
                for header in headers:
                    share[header] = line[index]
                    index += 1
        
                shares.append(share)
        cost = 0
        for share in shares:
            cost += float(share['price']) * float(share ['shares'])
            print(share.get('prizeee', "None"))

        print(f'Total cost of portfolio: {cost}')
    except ValueError:
        print("FFFF")


def six_two():
    import gzip
    with gzip.open('./Data/portfolio.csv.gz', 'rt') as file:
        for line in file:
            print(line)

def sets():
    test = {
            "john": 69
            }
    s1 = set([1,3,7,8])
    s2 = set([2,6,7,8,9,5]) 
    print(f'Union: {s1 | s2} \nIntersection: {s1 & s2} \nDifference: {s1 - s2}')
    print('iets' in test)

def read_csv(filename):
    import csv

    portfolio = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            share = ()
            for item in row:
                share += (item, )
            portfolio.append(share)

    return portfolio

def main():
    from collections import Counter
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    portfolio = read_csv(filename)

    holdings = Counter()
    for entry in portfolio:
        name, shares, price = entry
        holdings[name] += int(shares)

    print(holdings)

main()
