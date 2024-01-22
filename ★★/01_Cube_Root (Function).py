def sqrt_n_times(x, n):
    return x ** 0.5 ** n

def cube_root(y):
    result = sqrt_n_times(y, 2)
    count = 2
    while count <= 32:
        result *= sqrt_n_times(result, count)
        count *= 2
    return result

def main():
    q = float(input())
    print(cube_root(q))

exec(input())
