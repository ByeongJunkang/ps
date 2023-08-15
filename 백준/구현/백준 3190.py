from collections import deque
N = int(input())
K = int(input())
apple_list = [list(map(int,input().split())) for _ in range(K)]
L = int(input())
dir_list = []
for _ in range(L):
    a,b = input().split()
    dir_list.append((int(a),b))
    
q= deque()
q.append((1,1))
count = 0
cur_cor = 0
time = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
x,y = 1,1
while True:
    next_x,next_y = x + dx[cur_cor] , y +dy[cur_cor]
    if (next_x,next_y) in q or next_x > N   or next_y > N  or next_x <= 0 or next_y <=0:
        break
    q.append((next_x,next_y))
    is_apple = False
    for item in apple_list:
        if item[0] == next_x and item[1] == next_y:
            apple_list.remove(item)
            is_apple = True
            break
    if is_apple == False:
        q.popleft()
    x,y = next_x,next_y
    count +=1 
    if count == dir_list[time][0]:
        if dir_list[time][1] == 'D':
            cur_cor = (cur_cor + 1) % 4
        else:
            cur_cor = (cur_cor -1) % 4
        
        if time + 1 < len(dir_list):
            time +=1

     
print(count+1)


    
