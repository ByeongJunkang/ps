# recommend 1 - > 가장 어려운 문제, 어려운 문제가 많은 경우 문제 번호가 큰 것 출력
# recommend -1 -> 가장 쉬운 문제, 쉬운 문제가 많은 경우 문제 번호가 작은 것 출력

# add P L -> 난이도가 L인 문제 번호 P 추가

# sovle P -> 추천 문제 리스트에서 문제 번호 P 제거 

import heapq,sys
input = sys.stdin.readline
n = int(input())
min_line = []
max_line = []
question_list = set()
for _ in range(n):
    #p = 문제 번호, l = 난이도
    p,l =map(int,input().split())
    heapq.heappush(min_line,(l,p))
    heapq.heappush(max_line,(-l,-p))
    question_list.add(p)

m = int(input())

for _ in range(m):
    cmd = list(input().split())
  
    if cmd[0] == "add":
        while True:
            number = heapq.heappop(min_line)
            if number[1] in question_list:
                heapq.heappush(min_line,number)
                break

        while True:
            number = heapq.heappop(max_line)
            if -(number[1]) in question_list:
                heapq.heappush(max_line,number)
                break
        heapq.heappush(min_line,(int(cmd[2]),int(cmd[1])))
        heapq.heappush(max_line,(-int(cmd[2]),-int(cmd[1])))
        question_list.add(int(cmd[1]))
    elif cmd[0] == "solved":
        question_list.remove(int(cmd[1]))

    elif cmd[0] == "recommend":
        if cmd[1] == "-1":
            while True:
                number = heapq.heappop(min_line)
                if number[1] in question_list:
                    heapq.heappush(min_line,number)
                    break
            print(min_line[0][1])
           
        elif cmd[1] == "1":
            while True:
                number = heapq.heappop(max_line)
                if -(number[1]) in question_list:
                    heapq.heappush(max_line,number)
                    break
            print(-max_line[0][1])
        

