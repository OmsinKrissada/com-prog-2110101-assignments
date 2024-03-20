d, m, y = [int(input()) for _ in range(3)]
y -= 543

if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    days_in_feb = 29
else:
    days_in_feb = 28
days_in_month = [31, days_in_feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(sum(days_in_month[: m - 1]) + d)
