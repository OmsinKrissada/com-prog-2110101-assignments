def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_coprime(a, b, c):
    return 1 == gcd(gcd(a, b), c)


def primitive_Pythagorean_triples(max_len):
    triple = []
    for high in range(max_len + 1):
        sub_triple = [high]
        back = high
        while back >= 3:
            if (
                len(sub_triple) == 1
                and gcd(high, back) == 1
                or len(sub_triple) == 2
                and is_coprime(sub_triple[0], sub_triple[1], back)
                and sub_triple[1] ** 2 + back**2 == sub_triple[0] ** 2
            ):
                if len(sub_triple) == 2:
                    triple.append([back, sub_triple[1], sub_triple[0]])
                else:
                    sub_triple.append(back)
            if len(sub_triple) == 2 and (
                sub_triple[1] ** 2 + back**2 < sub_triple[0] ** 2 or back == 3
            ):
                sub_triple[1] -= 1
                back = sub_triple[1]
            back -= 1

    return triple


exec(input().strip())
