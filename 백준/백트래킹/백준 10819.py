from itertools import permutations

N = int(input())
num = sorted(list(map(int,input().split())))
result = []
def check(result):
    answer = 0
    for i in range(N-1):
        answer += abs(result[i]-result[i+1])
    return answer

max_num = -10e9
def permutation():
    global max_num
    if len(result) == N:
        result1 = [0] * N
        for j in range(N):
            result1[j] = num[result[j]]
        answer = check(result1)
        max_num = max(max_num,answer)
        return
    for i in range(len(num)):
        if i not in result:
            result.append(i)
            permutation()
            result.pop()

permutation()
print(max_num)