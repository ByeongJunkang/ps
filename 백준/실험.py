# def dfs(length):
#     letter = ["A","E","I","O","U"]
#     tmp = []
#     print(tmp)
#     if len(tmp) == length:
#         return
#     for i in letter:
#         tmp.append(i)
#         dfs(length)
#         tmp.pop()

# dfs(1)


# import heapq,math,sys

# distance = [math.inf] * 1001
# input = sys.stdin.readline
# n,e = map(int,input().split())
# graph = [[]  for _ in range(n+1)]

# for _ in range(e):
#     a,b,c = map(int,input().split())
#     graph[a].append((b,c))
#     graph[b].append((a,c))


# def disk(start):

#     distance[start] = 0

#     q = []
#     heapq.heappush(q,(start,0))

#     while q:
#         now,length = heapq.heappop(q)

#         if distance[now] < length:
#             continue

#         for i in graph[now]:
#             cost = i[1] + length
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q,(i[0],cost))


from itertools import combinations_with_replacement,combinations,product,permutations

# print(list(combinations_with_replacement([1,2,3],3)))
# print(list(combinations([1,2,3],3)))
print(list(product([1,2,3],repeat=3)))
# print(list(permutations([1,2,3],3)))