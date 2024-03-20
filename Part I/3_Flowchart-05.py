c = input()
if c == 'S':
    m = int(input())
    r = i = 0
    q = t = k = 1
    n = x = 3
    p = ''
    while i < m:
        if 4*q + r - t < n*t:
            p = p + str(n)
            i = i + 1
            a = 10*(r - n*t)
            n = 10*(3*q + r)//t - 10*n
            q = 10*q
            r = a
        else:
            a = (2*q+r)*x
            b = (7*q*k+2+x*r)//(x*t)
            q = k*q
            t = x*t
            x = x+2
            k = k+1
            n = b
            r = a
    p = p[0] + '.' + p[1:]
    print(f'pi = {p}')
elif c == 'R':
    n = int(input())
    sum_val = 0
    for k in range(n+1):
        sum_val += ((-3)**(-k))/(2*k+1)
    p = round(12**(1/2)*sum_val, 12)
    print(f'pi = {p}')
elif c == 'P':
    p = round((7+(6+5**(1/2))**(1/2))**(1/2), 6)
    print(f'pi = {p}')
else:
    print('Invalid')