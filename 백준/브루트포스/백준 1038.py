N = int(input())
result = []
answer = []
def dfs(prev,num):
    if len(result) == num:
        num_str = ''.join(map(str, result))
        answer.append(int(num_str))
        return

    for k in range(10):
        if k < prev and k not in result:
            result.append(k)
            dfs(k,num)
            result.pop()

for i in range(1,11):
    dfs(10,i)

if N > len(answer) - 1:
    print(-1)
else:
    print(answer[N])

