N = int(input())
left_arm,right_arm , waist ,left_leg ,right_leg = 0,0,0,0,0
cookie = [list(input()) for _ in range(N)]
location = []
count = 0
istrue = False
for i in range(N):
    for j in range(N):
        if cookie[i][j] == '*' and count == 0:
            location.append(i+1)
            location.append(j)
            count +=1
            break
heart_x, heart_y = location[0],location[1]
for k in range(heart_y):
    if cookie[heart_x][k] == '*':
        left_arm +=1

for k in range(heart_y+1,N):
    if cookie[heart_x][k] == '*':
        right_arm +=1


for k in range(heart_x+1,N):
    if cookie[k][heart_y] == '*':
        waist+=1
    else:
        break

for k in range(heart_x+waist+1,N):
    if cookie[k][heart_y-1] == '*':
        left_leg +=1
    else:
        break

for k in range(heart_x+waist+1,N):
    if cookie[k][heart_y+1] == '*':
        right_leg +=1
    else:
        break
print(heart_x+1, end=" ")
print(heart_y+1)
print(left_arm,end = " ")
print(right_arm, end = " ")
print(waist,end=" ")
print(left_leg,end=" ")
print(right_leg)

