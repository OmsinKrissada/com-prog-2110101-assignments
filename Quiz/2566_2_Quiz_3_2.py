def read_friends():
    dat = []
    N = int(input())
    for i in range(N):
        dat.append(tuple(input().strip().split()))
    return dat

def count_friends(data, names):
    friends = {}
    for name in names:
        if name not in friends:
            friends[name] = set()
        for pair in data:
            if name in pair:
                friend = pair[1] if pair[0] == name else pair[0]
                friends[name].add(friend)
    return sorted([(n, len(friends[n])) for n in names])

exec(input().strip())
