import math

a, b, c = input().split(",")
combined = f"{a}.{b}"
bottom = 10 ** len(b)
top = int(float(combined) * bottom)

top = top * int("9" * len(c)) * 10 ** len(b) + int(c) * bottom
bottom = bottom * int("9" * len(c)) * 10 ** len(b)
gcd = math.gcd(top, bottom)
print(f"{top // gcd} / {bottom // gcd}")
