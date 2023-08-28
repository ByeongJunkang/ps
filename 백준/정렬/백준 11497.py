import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    tree = list(map(int,input().split()))
    tree.sort()
    new_tree =[]
    for i in range(N):
        if i%2 ==0:
            new_tree.append(tree[i])
    for i in range(N-1,-1,-1):
        if i % 2 == 1:
            new_tree.append(tree[i])
    ans = 0
    for i in range(N):
        ans = max(ans,abs(new_tree[i]-new_tree[i-1]))
    
    print(ans)