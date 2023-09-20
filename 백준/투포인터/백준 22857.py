import sys
input = sys.stdin.readline
n, k = map(int,input().split())
num = list(map(int,input().split()))
start, end, odd,ans= 0,0,0,0
while end <n:
    if num[end] % 2 == 1:
        if odd < k:
            odd +=1
        elif odd == k:
            while True:
                if num[start] %2 ==1:
                    start +=1
                    break
                start +=1    
    end +=1
    ans = max(ans,end-start-odd)
print(ans)