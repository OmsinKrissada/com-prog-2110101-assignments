coupons = []

for i in range(int(input())):
    name, price = input().strip().split()
    coupons.append((int(price), name))

coupons.sort()
coupons.reverse()

taken = {}
pocket = int(input())
init_pocket = pocket

current_coupon_idx = 0
while current_coupon_idx < len(coupons):
    this_coupon = coupons[current_coupon_idx]
    if this_coupon[0] <= pocket and (
        this_coupon[1] not in taken or taken[this_coupon[1]] < 3
    ):
        if this_coupon[1] in taken:
            taken[this_coupon[1]] += 1
        else:
            taken[this_coupon[1]] = 1
        pocket -= this_coupon[0]
    else:
        current_coupon_idx += 1

print(">", init_pocket, init_pocket - pocket, pocket)

if init_pocket == pocket:
    print("No coupon")
else:
    for name, v in sorted(list(taken.items())):
        print(name, v)
