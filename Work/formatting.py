#!/bin/python
def format_numbers():
    value = 3650.3
    print(f'{value:->16,.4f}')
    print(f'{value:>16.2f}')
    print(f'{value:<16.2f}')
    print(f'{value:*>16,.2f}')

def read_portfolio(filename):
    try:
        with open(filename, 'rt') as file:
            headers = next(file).replace("\n","").split(",")
            shares = []
            for line in file:
                line = line.replace("\n","").split(",")
                shares.append(tuple(line))
        cost = 0
        for share in shares:
            name, amount, price = share
            cost += float(price) * float(amount)

        print(f'Total cost of portfolio: {cost}')
        return shares
    except ValueError:
        print("FFFF")


def make_report(portfolio, prices):
    matched_prices = []
    for entry in portfolio:
        name, amount, price = entry 
        for price in prices:
            if name in price:
                matched_prices.append(price)
    headers = ("Name", "Shares", "Price", "Change")
    name, shares, price, change = headers
    print(f'{name:>8}{shares:>8}{price:>8}{change:>8}')
    print(f'{"":->8}{"":->8}{"":->8}{"":->8}')

    index = 0
    for share in matched_prices:
        matched_name, new_price = share
        name, amount, price = portfolio[index]
        difference = float(new_price) - float(price)
        print(f'{name:>8}{amount:>8}{float(new_price):>8,.2f}${difference:>8,.2f}$')
        index += 1

def read_prices(filename):
    prices = []
    with open(filename, 'rt') as file:
        for line in file:
            prices.append(tuple(line.replace("\n","").split(",")))
    return prices

def main():
    portfolio = read_portfolio("./Data/portfolio.csv")
    prices = read_prices("./Data/prices.csv")
    make_report(portfolio, prices)
main()
