
N = int(input())
num =list((map(int,input().split())))
plus,minus,mul,div = map(int,input().split())
answer = []
def solution(start,result):
    global plus,minus,mul,div
    if start == N:
        answer.append(result)
        return
    else:
        if plus > 0:
            plus -=1
            solution(start+1,result + num[start])
            plus += 1
        if minus > 0:
            minus -=1
            solution(start+1,result - num[start])
            minus += 1
        if mul > 0:
            mul -=1
            solution(start+1,result * num[start])
            mul += 1
        if div >0:
            div -=1
            solution(start+1,int(result / num[start]))
            div +=1
        

solution(1,num[0])
print(max(answer))
print(min(answer))