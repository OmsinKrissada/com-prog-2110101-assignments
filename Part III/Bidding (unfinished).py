products = {}

for round in range(int(input())):
    raw = input().split()
    # if raw[0] not in ['B','W']:
        # continue
    op = raw.pop(0)

    if op == 'B':
        bidder,prod,amt = raw
        amt = int(amt)
        if prod in products:
            if products[prod][1] < amt:
                products[prod] = (bidder,amt)
        else:
            products[prod] = (bidder,amt)
    elif op == 'W':
        bidder, prod = raw
        if prod in products and products[prod][0] == bidder:
            del products[prod]
    print(products)

print(products)