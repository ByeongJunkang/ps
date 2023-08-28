N = int(input())
P = list(map(int,input().split()))
new_p = sorted(P)
time = 0
for i in range(N):
    time += (N - i) * new_p[i]
print(time)