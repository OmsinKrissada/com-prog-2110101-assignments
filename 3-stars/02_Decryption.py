x = input()
every_7 = x[3::7]
every_5 = x[7::5]
first_sum = int(every_5) + int(every_7) + 10000
digit_slice = str(first_sum)[-4:-1]
second_sum = sum([int(n) for n in digit_slice]) % 10 + 1
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(digit_slice + letters[second_sum - 1])
