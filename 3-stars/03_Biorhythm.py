import math

bd, bm, by, d, m, y = [int(e) for e in input().split()]


def sum_days_in_month(d, m, y, from_end=False):
    y -= 543
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        days_in_feb = 29
    else:
        days_in_feb = 28
    days_in_month = [31, days_in_feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    sliced = days_in_month[: m - 1] if not from_end else days_in_month[m:]
    return sum(sliced) + (d if not from_end else days_in_month[m - 1] - d)


total = (
    sum_days_in_month(bd, bm, by, True)
    + 365 * (y - by - 1)
    + sum_days_in_month(d, m, y)
)

print(total, end=" ")
print("{:.2f}".format(math.sin(2 * math.pi * total / 23)), end=" ")
print("{:.2f}".format(math.sin(2 * math.pi * total / 28)), end=" ")
print("{:.2f}".format(math.sin(2 * math.pi * total / 33)))
