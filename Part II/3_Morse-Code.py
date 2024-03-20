with open(input()) as f:
    op = f.readline().strip()
    raw_mapping = f.readline().strip()
    todos = f.read().splitlines()

    mapping = {}
    for current in raw_mapping.split("[")[1:-1]:
        if op == "T2M":
            mapping[current[0]] = current[2:]
        elif op == "M2T":
            mapping[current[2:]] = current[0]

    if op in ["T2M", "M2T"]:
        for line in todos:
            combined = []
            is_valid = True
            for letter in line if op == "T2M" else line.split():
                if letter in mapping:
                    combined.append(mapping[letter])
                else:
                    is_valid = False
                    break
            if is_valid:
                print((" " if op == "T2M" else "").join(combined))
            else:
                print(f"Invalid : {line}")
    else:
        print("Invalid code")
