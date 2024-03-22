filename = input()
teacher = input()

sections = []
f_count = m_count = 0
with open(filename) as f:
    lines = f.read().splitlines()
    for line in lines:
        fields = line.split(",")
        if fields[4] == teacher:
            if fields[3] not in sections:
                sections.append(fields[3])
            if fields[1] == "F":
                f_count += 1
            else:
                m_count += 1

sections.sort()

if len(sections) == 0:
    print("Not found")
else:
    label = "Section" + ("s" if len(sections) > 1 else "")
    print(f'{label}: {",".join(sections)} --> F = {f_count}, M = {m_count}')
