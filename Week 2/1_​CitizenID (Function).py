def check_digit(n):
    mids = [int(d) for d in n]
    the_sum = sum([mids[i] * (13 - i) for i in range(12)])
    return (11 - the_sum % 11) % 10

exec(input())
