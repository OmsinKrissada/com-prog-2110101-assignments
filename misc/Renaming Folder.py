filename, pattern, replace = [input() for _ in range(3)]

def match(text, the_pattern):
    if len(text) != len(the_pattern):
        return False
    for t, p in zip(text, the_pattern):
        if p == '?':
            continue
        if t.lower() != p.lower():
            return False
    return True

with open(filename, 'r') as f:
    for line in f:
        buffer = ''
        for char in line:
            if char == '/':
                if match(buffer, pattern):
                    print(replace, end='')
                else:
                    print(buffer, end='')
                buffer = ''
                print('/', end='')
            else:
                buffer += char
        print(buffer, end='')
