import math
n = int(input())
left = math.sqrt(2*math.pi) * n**(n+0.5) * math.e**-n

print(left * math.e**(1/(12*n+1)))
print(left * math.e**(1/(12*n)))
