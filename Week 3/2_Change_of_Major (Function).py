def choose(student1, student2):
    s1_pass = s2_pass = False

    if student1[2] == "A" and student1[3] <= "C" and student1[4] <= "C":
        s1_pass = True
    if student2[2] == "A" and student2[3] <= "C" and student2[4] <= "C":
        s2_pass = True

    if s1_pass and s2_pass:
        combined1 = str(student2[1]) + student1[3] + student1[4]
        combined2 = str(student1[1]) + student2[3] + student2[4]
        if combined1 == combined2:
            return [student1[0], student2[0]]
        elif combined1 < combined2:
            return [student1[0]]
        else:
            return [student2[0]]
    elif s1_pass:
        return [student1[0]]
    elif s2_pass:
        return [student2[0]]
    else:
        return []


exec(input())
