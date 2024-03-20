products = {}

for i in range(int(input())):
    name, price = input().split()
    products[name] = float(price)

total = 0
sold = {}
for i in range(int(input())):
    name, amount = input().split()
    amount = float(amount)
    if name in products:
        total += products[name] * amount
        if name in sold:
            sold[name] += amount
        else:
            sold[name] = amount

if total == 0:
    print("No ice cream sales")
else:
    print(f"Total ice cream sales: {total}")
    transformed = [[val * products[key], key] for key, val in sold.items()]
    transformed.sort()
    transformed.reverse()
    maxes = []
    max_val = transformed[0][0]
    for sale, name in transformed:
        if max_val != sale:
            break
        maxes.append(name)

    print(f'Top sales: {", ".join(sorted([x for x in maxes]))}')
