import math

a = float(input())
b = float(input())
c = float(input())

root = math.sqrt(b**2 - 4*a*c)

print(round((-b-root)/(2*a),3), end=' ')
print(round((-b+root)/(2*a),3))
