words = ["soon", "neung", "song", "sam", "si", "ha", "hok", "chet", "paet", "kao", "sip"]

def digit(n, d):
    return n // 10**d % 10

def to_Thai(N):
    if N == 0:
        return "soon"
    constructed = []
    if digit(N, 3) != 0:
        constructed.append(words[digit(N, 3)])
        constructed.append("pun")
    if digit(N, 2) != 0:
        constructed.append(words[digit(N, 2)])
        constructed.append("roi")
    if digit(N, 1) != 0:
        if digit(N, 1) == 1:
            pass
        elif digit(N, 1) == 2:
            constructed.append("yi")
        else:
            constructed.append(words[digit(N, 1)])
        constructed.append("sip")
    if digit(N, 0) != 0:
        if digit(N, 0) == 1 and digit(N, 1) + digit(N, 2) + digit(N, 3) != 0:
            constructed.append("et")
        else:
            constructed.append(words[digit(N, 0)])
    return " ".join(constructed)


exec(input().strip())
