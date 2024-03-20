def is_odd(n):
    return n % 2 == 1


def has_odds(x):
    for n in x:
        if is_odd(n):
            return True
    return False


def all_odds(x):
    for n in x:
        if not is_odd(n):
            return False
    return True


def no_odds(x):
    for n in x:
        if is_odd(n):
            return False
    return True


def get_odds(x):
    out = []
    for n in x:
        if is_odd(n):
            out.append(n)
    return out


def zip_odds(a, b):
    filtered_a = get_odds(a)
    filtered_b = get_odds(b)
    out = []
    for i in range(max(len(filtered_a), len(filtered_b))):
        if i < len(filtered_a):
            out.append(filtered_a[i])
        if i < len(filtered_b):
            out.append(filtered_b[i])
    return out


exec(input().strip())
