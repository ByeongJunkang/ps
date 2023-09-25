xs,ys = map(int,input().split())
xe,ye = map(int,input().split())
tp = [list(map(int,input().split())) for _ in range(3)]
ans = abs(xs-xe) + abs(ys-ye)
visited = set()
def dfs(x,y,cnt,dis):
    global ans
    ans = min(ans,cnt * 10 + abs(x-xe) + abs(y-ye) + dis)
    for tmp in tp:
        x1,y1,x2,y2 = tmp[0],tmp[1],tmp[2],tmp[3]
        time1 = abs(x-x1) + abs(y-y1)
        time2 = abs(x-x2) + abs(y-y2)
        if time1 < time2:
            if (x2,y2) and (x1,y1) not in visited:
                visited.add((x2,y2))
                visited.add((x1,y1))
                dfs(x2,y2,cnt+1,dis+time1)
                visited.remove((x2,y2))
                visited.remove((x1,y1))
        else:
            if (x1,y1) and (x2,y2) not in visited:
                visited.add((x1,y1))
                visited.add((x2,y2))
                dfs(x1,y1,cnt+1,dis+time2)
                visited.remove((x1,y1))
                visited.remove((x2,y2))

dfs(xs,ys,0,0)
print(ans)