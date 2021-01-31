#!/bin/python
def six_one():
    with open('./Data/portfolio.csv', 'rt') as file:
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

    print(f'Total cost of portfolio: {cost}')

def six_two():
    import gzip
    with gzip.open('./Data/portfolio.csv.gz', 'rt') as file:
        for line in file:
            print(line)

six_two()

