from itertools import combinations
num = [1,2,3,4]
num1 = [1,2, 3, 5, 8, 13, 21, 34]
arr= []
out = []
def permutation(start,idx):
    if start == 6:
        print(*arr)
        return
    
    for i in range(idx,7):
        if num[i] not in arr:
            arr.append(num[i])
            permutation(start+1,idx+1)
            arr.pop()

permutation(0,0)
def dfs(idx):
    if len(out) == 3:
        print(*out)
        return

    for i in range(idx, 4):
        out.append(num[i])
        dfs(i + 1)
        out.pop()


dfs(0)

# while True:
#     num = list(map(int,input().split()))
#     if len(num) == 1:
#         break
#     else:
#         num.pop(0)
#         a = list(combinations(num,6))
#         for i in a:
#             print(*i)
#         print()


