N,K = map(int,input().split())
min_weight = 500
exercise = list(map(int,input().split()))
#K는 중량 감소
#N은 운동 키트

weight_list = []
result = []
def permutation():
    if len(result) == N:
        weight_list.append(result[:])
        return
    for i in range(N):
        if i not in result:
            result.append(i)
            permutation()
            result.pop()

permutation()
answer = 0
for i in weight_list:
    isTrue = True
    cur_weight = min_weight
    for weight_num in i:
        cur_weight = cur_weight + exercise[weight_num] - K
        if cur_weight < min_weight:
            isTrue = False
            break
    if isTrue:
        answer+=1
print(answer)