# # import sys
# # sys.setrecursionlimit(10**9)
# # n, m = map(int,input().split())
# # graph = [[0] *(n+1) for _ in range(n+1)]
# # visited = [[0] * (n+1) for _ in range(n+1)]
# # graph_dic = [0] * (n+1)

# # for _ in range(m):
# #     a,b = map(int,input().split())
# #     graph[a][b]= 1

# # num = [0] * (n+1)
# # S,T = map(int,input().split())


# # result = []
# # def dfs(a,t,k):
# #     if a == t:
# #         for i in result:
# #             if num[i] < k and num[i] >= k-1:
# #                 num[i] = k
# #         return
# #     for i in range(len(graph[a])):
# #         if visited[a][i] == 0 and graph[a][i] == 1:
# #             visited[a][i] = 1
# #             result.append(i)
# #             dfs(i,t,k)
# #             result.pop()
# #             visited[a][i] = 0 

          
# # dfs(S,T,1)
# # visited = [[0] * (n+1) for _  in range(n+1)]
# # dfs(T,S,2)
# # answer= 0
# # for i in range(len(num)):
# #     if i == S or i == T:
# #         continue
# #     if num[i] == 2:
# #         answer +=1

# # print(answer)

# import sys
# sys.setrecursionlimit(10**9)
# n, m = map(int,input().split())
# graph = [[] for _ in range(n+1)]
# visited = [[] for _ in range(n+1)]
# for _ in range(m):
#     a,b = map(int,input().split())
#     graph[a].append(b)
#     visited[a].append(False)

# num = [0] * (n+1)
# S,T = map(int,input().split())

# result = []
# def dfs(a,t,k):
#     if a == t:
#         for i in result:
#             if num[i] < k and num[i] >= k-1:
#                 num[i] = k
#         return
#     for i in range(len(graph[a])):
#         if visited[a][i] == False:
#             result.append(graph[a][i])
#             visited[a][i] = True
#             dfs(graph[a][i],t,k)
#             result.pop()
#             visited[a][i] = False

          
# dfs(S,T,1)
# dfs(T,S,2)
# answer= 0
# for i in range(len(num)):
#     if i == S or i == T:
#         continue
#     if num[i] == 2:
#         answer +=1

# print(answer)


# sys.stdin=open('input.txt','r')

def DFS(now, adj, visit):
    if visit[now]==1:
        return
    else:
        visit[now]=1
        for neighbor in adj[now]:
            DFS(neighbor, adj, visit)
    return

if __name__=="__main__":
    n,m=map(int, input().split())   # 정점, 간선 
    adj=[[] for _ in range(n+1)]    # 노드별 이동 가능한 노드들 정보
    adjR=[[] for _ in range(n+1)]   # adj_reverse
    for _ in range(m):
        a,b,=map(int,input().split())
        adj[a].append(b)    # a노드에서 b노드로 갈수 있음
        adjR[b].append(a)
    S,T=map(int, input().split())   # S->T S가 집 T가 회사


    
    # 목적: S->T와 T->S로 모두에서 방문 가능한 정점의 개수를 출력한다.
    fromS=[0]*(n+1)
    fromS[T]=1          # S->T 1로 미리 세팅
    DFS(S,adj,fromS)

    fromT=[0]*(n+1)
    fromT[S]=1          # T->S 1로 미리 세팅
    DFS(T,adj,fromT)

    toS=[0]*(n+1)
    DFS(S,adjR,toS)

    toT=[0]*(n+1)
    DFS(T,adjR,toT)
    
    count=0
    for i in range(1,n+1):
        if fromS[i] and fromT[i] and toS[i] and toT[i]: # 이렇게가는거랑 저렇게 가는거랑 모두 1일때만
            count+=1

    print(count-2)