N=int(input())
num = sorted(list(map(int,input().split())))
num_list = list(map(int,input().split()))
num_list.sort(reverse=True)

ans = 0
for i in range(N):
    ans += num[i] * num_list[i]
print(ans)