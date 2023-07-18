n,d,k,c = map(int,input().split())

# n = 접시의 수
# d = 초밥의 가짓수
# k = 연속해서 먹는 접시의 수
# c = 쿠폰 번호
num = []
count = [0] * (d+1) 
for _ in range(n):
    a = int(input())
    num.append(a)

count[c] = 1 
chobab = 1
for i in range(k):
    if num[i] != c:
        count[num[i]] +=1
    if count[num[i]] == 1 and num[i] !=c :
        chobab +=1 
answer = [chobab]
start = 0
end = k-1
while True:
   
    end+=1
    if end +1 >n:
        end = (end) %n
    if count[num[start]] > 1:
        if num[start] != c:
            count[num[start]] -=1
    
    else:
        if num[start] !=c:
            count[num[start]] -=1
            chobab-=1

    if count[num[end]] !=c:
        count[num[end]] +=1

    if count[num[end]] <=1:
            if num[end] !=c:
                chobab +=1
    start+=1
    if start + 1 > n:
        start = (start  %n)

    answer.append(chobab)
    if end == k-1:
        break
print(max(answer))
    


#다른 사람 풀이

# import sys
# def input(): return sys.stdin.readline().rstrip()

# n,d,k,c=map(int,input().split())

# rotatesusi=[int(input()) for i in range(n)]

# x,y=0,0
# susidict={}
# meatsusi=0

# while y<k:
#     if rotatesusi[y] not in susidict.keys():
#         susidict[rotatesusi[y]]=1
#     else:
#         susidict[rotatesusi[y]]+=1
#     y+=1
# if c not in susidict.keys():
#     susidict[c]=1
# else:
#     susidict[c]+=1
# while x<n:
#     meatsusi=max(meatsusi,len(susidict))

#     susidict[rotatesusi[x]]-=1
#     if susidict[rotatesusi[x]]==0:
#         del susidict[rotatesusi[x]]
#     if rotatesusi[y%n] not in susidict.keys():
#         susidict[rotatesusi[y%n]]=1
#     else:
#         susidict[rotatesusi[y%n]]+=1

#     x+=1
#     y+=1
# print(meatsusi)
