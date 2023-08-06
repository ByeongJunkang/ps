# n = int(input())
# ans = 0
# row = [0] * n

# def is_promising(x):
#     for i in range(x):
#         if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
#             return False
    
#     return True

# def n_queens(x):
#     global ans
#     if x == n:
#         ans += 1
#         return

#     else:
#         for i in range(n):
#             # [x, i]에 퀸을 놓겠다.
#             row[x] = i
#             if is_promising(x):
#                 n_queens(x+1)

# n_queens(0)
# print(ans)


N = int(input())
visited = [0] * (N)

answer = 0
result = []
def n_queen(num,last_num):

    global answer
    if num == N:
        answer +=1
        print(visited)
        print(result)
        return

    for i in range(N):
        if not visited[i]:
            if i >= last_num+4 or i <= last_num -4:
                visited[i] = True
                result.append(i)
                n_queen(num+1,i)
                visited[i] = False
                result.pop()
    
for i in range(1,N-1):
    visited[i] = True
    n_queen(1,i)
    visited[i] = False

print(answer)
