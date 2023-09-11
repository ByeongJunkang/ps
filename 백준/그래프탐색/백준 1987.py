R,C = map(int,input().split())
board = [list(input()) for _ in range(R)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
max_result = 0
result = set()
def dfs(i,j,cnt):
    global max_result 
    max_result = max(max_result,cnt)
    result.add(board[i][j])
    for num in range(4):
        next_x = i + dx[num]
        next_y = j + dy[num]
        if 0 <= next_x < R and 0 <= next_y < C:
            if board[next_x][next_y] not in result:
                dfs(next_x,next_y,cnt+1)
    # discard를 remove로..
    result.remove(board[i][j])



dfs(0,0,1)
print(max_result)
