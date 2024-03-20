def check_digit(n):
    mids = [int(d) for d in n]
    the_sum = sum([mids[i] * (13 - i) for i in range(12)])
    return (11 - the_sum % 11) % 10

n = input()
n += str(check_digit(n))
space_after = [0, 4, 9, 11]

for i in range(13):
    print(n[i], end="")
    if i in space_after:
        print(end=" ")
