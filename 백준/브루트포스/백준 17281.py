from itertools import permutations
import sys
input = sys.stdin.readline
N= int(input())
bat = [list(map(int,input().split())) for _ in range(N)]
max_score = 0
for line_up in permutations((range(1 , 9)), 8):
    line_up = list(line_up[:3]) + [0] + list(line_up[3:])  
    score = 0
    order = 0
    for inning in range(N):
        out_count = 0
        base1, base2, base3 = 0, 0, 0
        while out_count < 3: 
            hit = bat[inning][line_up[order]]
            if hit == 0:
                out_count +=1
            elif hit == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif hit == 2:
                score += (base2 + base3)
                base1, base2, base3 = 0, 1, base1
            elif hit == 3:
                score += (base1 + base2 + base3)
                base1, base2, base3 = 0, 0, 1
            elif hit == 4:
                score += (base1 + base2 + base3 + 1)
                base1, base2, base3 = 0, 0, 0
            order = (order + 1) % 9
    max_score = max(score,max_score)

print(max_score)


# def dfs():
#     global max_score
#     if len(result) == 8:
#         real_result.append( result[:3] + [0] + result[3:8])
#         return
#     for i in range(1,9):
#         if i not in result:
#             result.append(i)
#             dfs()
#             result.pop()
# dfs()