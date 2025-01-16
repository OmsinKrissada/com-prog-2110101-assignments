idols_stat = {}  # idol: score, voted_by
ota_kami = {}  # ota: (idol: votes)

while True:
    inp = input()
    if inp == "1":
        converted = list(idols_stat.items())
        converted.sort(reverse=True, key=lambda x: x[1][0])
        print(", ".join([x[0] for x in converted[:3]]))
        break
    if inp == "2":
        converted = list(idols_stat.items())
        converted.sort(reverse=True, key=lambda x: len(x[1][1]))
        print(", ".join([x[0] for x in converted[:3]]))
        break
    if inp == "3":
        kami_count = {}
        for key in idols_stat:
            kami_count[key] = 0
        for idols in ota_kami.values():
            highest = ""
            at = 0
            for idol, vote in idols.items():
                if vote > at:
                    highest = idol
                    at = vote
                elif vote == at:
                    highest = min(idol, highest)
            kami_count[highest] += 1

        counts = list(kami_count.items())
        counts.sort(reverse=True, key=lambda x: x[1])
        print(", ".join([x[0] for x in counts[:3]]))
        break

    ota, idol, vote = inp.split(" ")
    vote = int(vote)

    if idol not in idols_stat:
        idols_stat[idol] = [0, set()]
    if ota not in ota_kami:
        ota_kami[ota] = {}

    idols_stat[idol][0] += vote
    idols_stat[idol][1].add(ota)

    ota_kami[ota][idol] = ota_kami[ota].get(idol, 0) + vote
