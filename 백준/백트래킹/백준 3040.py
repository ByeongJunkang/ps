from itertools import combinations
dwarf = [int(input()) for _ in range(9)]
tmp_num =[i for i in range(9)]
for tmp_dwarf in list(combinations(tmp_num,7)):
    tmp = []
    for idx in range(7):
        tmp_idx = tmp_dwarf[idx]
        tmp.append(dwarf[tmp_idx])
    if sum(tmp) == 100:
        for dwarfs in tmp:
            print(dwarfs)
        break