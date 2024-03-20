x=input()
h=int(x)
for line in range(1, h):
    print("-" * (h-line), end="")
    print("*", end="")
    print("-" * (2*line-3), end="")
    print("" if line==1 else "*")
print("*" * (2*h-1))
