import sys

N = int(input())
marathon = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]



max_num = 0
max_index = 0
for i in range(1,N-1):
    diff = abs(marathon[i][0]-marathon[i-1][0]) + abs(marathon[i][1]-marathon[i-1][1]) + abs(marathon[i+1][1]- marathon[i][1])+ abs(marathon[i][0]-marathon[i+1][0])
    straight = abs(marathon[i+1][0]-marathon[i-1][0]) + abs(marathon[i+1][1] - marathon[i-1][1])
    skip = diff - straight
    max_num = max(max_num,skip)
    

sum = 0

for i in range(N-1):
    sum = sum + abs(marathon[i+1][1]- marathon[i][1])+ abs(marathon[i][0]-marathon[i+1][0])
   
    
print(sum - max_num) 