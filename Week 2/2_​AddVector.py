u = [float(x) for x in input()[1:-1].split(", ")]
v = [float(x) for x in input()[1:-1].split(", ")]

print(f"{u} + {v} = {[u[i] + v[i] for i in range(3)]}")
