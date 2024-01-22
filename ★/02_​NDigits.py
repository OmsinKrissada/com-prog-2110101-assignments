n, digits = input(), int(input())
if digits < len(n):
    digits = len(n)
print(("0" * digits + n)[-digits:])
