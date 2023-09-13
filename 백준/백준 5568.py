import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
num_list = [int(input()) for _ in range(n)]
idx = [i for i in range(n)]
temp = []
result =set()
def dfs():
    if len(temp) == k:
        tmp_result = ''
        for i in range(k):
            tmp_result+=str(num_list[temp[i]])
        if tmp_result not in result:
            result.add(tmp_result)
        return
    
    for i in range(n):
        if idx[i] not in temp:
            temp.append(idx[i])
            dfs()
            temp.pop()

dfs()
print(len(result))