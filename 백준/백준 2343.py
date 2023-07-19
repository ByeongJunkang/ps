# N개의 강의
#  i,j 같은 불루레이 녹화 -> i,j 사이 모든 강의도 블루레이 녹화
# M개의 블루레이에 동영상 모두 녹화
# 블루레이 크기 최소
# M의 크기는 같음
# 강의 길이는 자연수
import sys
n,m = map(int,input().split())
num  = list(map(int,input().split()))
left = max(num)
right = sum(num)
answer = 0
while left <= right:
    mid = (left+right) //2
    sum = 0
    cnt = 0
    for i in range(n):
        if sum +  num[i]> mid:
            cnt +=1
            sum = 0
        sum +=num[i]
        

    if sum:
        cnt +=1 
    if cnt > m:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid
print(answer)