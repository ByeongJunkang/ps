#연비 1L
# 도시 하나의 주유소
# 리터 가격 다를 수 있음
# 단위는 원

import sys
input = sys.stdin.readline
N = int(input().rstrip())
city = list(map(int,input().split()))
fuel = list(map(int,input().split()))

answer = city[0] * fuel[0]
min_fuel = fuel[0]
for i in range(1,len(fuel)):
    min_fuel = min(min_fuel,fuel[i])
    if i == len(fuel) -1:
        continue
    else:
        next_city = city[i]
        answer += next_city * min_fuel
print(answer)

    