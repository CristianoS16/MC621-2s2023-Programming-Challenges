blimp_list = [input() for _ in range(5)]
cia_blimp = []

blimp_idx = 0
# Travels blimp_list and checks which one has "FBI"
while(blimp_idx < 5):
    if "FBI" in blimp_list[blimp_idx]:
        cia_blimp.append(blimp_idx+1)
    blimp_idx += 1
if len(cia_blimp) == 0:
    print("HE GOT AWAY!")
else:
    print(*cia_blimp)
