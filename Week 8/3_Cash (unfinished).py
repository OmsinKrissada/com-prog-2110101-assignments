def total(pocket):
    total = 0
    for c, v in pocket.items():
        total += c * v
    return total


def take(pocket, money_in):
    for c, amount in money_in.items():
        if c in pocket:
            pocket[c] += amount
        else:
            pocket[c] = amount


def pay(pocket, amt):
    owed = amt
    out = {}
    for c in pocket:
        if owed < c:
            continue
        if c in out:
            out[c] += 1
        else:
            out[c] = 1
        pocket[c] -= 1


# exec(input().strip())
p = {100: 2, 50: 2, 5: 2, 1: 2}
print(total(p))
