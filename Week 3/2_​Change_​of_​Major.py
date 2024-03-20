student1 = input().split()
student2 = input().split()

s1_pass = s2_pass = False
# preliminary checks
if student1[2] == "A" and student1[3] <= "C" and student1[4] <= "C":
    s1_pass = True
if student2[2] == "A" and student2[3] <= "C" and student2[4] <= "C":
    s2_pass = True

if s1_pass and s2_pass:
    combined1 = student2[1] + student1[3] + student1[4]
    combined2 = student1[1] + student2[3] + student2[4]
    if combined1 == combined2:
        print("Both")
    elif combined1 < combined2:
        print(student1[0])
    else:
        print(student2[0])
elif s1_pass:
    print(student1[0])
elif s2_pass:
    print(student2[0])
else:
    print("None")
