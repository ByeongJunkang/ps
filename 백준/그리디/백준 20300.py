N = int(input())
muscle = list(map(int,input().split()))
muscle.sort()
max_num = 0
if len(muscle)%2 == 1:
    for i in range(N//2):
        max_num = max(max_num,muscle[i]+muscle[N-2-i],muscle[-1])
else:
    for i in range(N//2):
        max_num = max(max_num,muscle[i]+muscle[N-1-i])

print(max_num)