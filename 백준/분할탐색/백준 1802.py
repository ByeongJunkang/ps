T = int(input())
import sys
sys.setrecursionlimit(10**9)
def search(arr,left,right,N):
    global res
    if N < 1 or left == right:
        return
    
    for i in range(N):
        if arr[left+i] == arr[right-i]:
            res+=1
            return  
    if res ==0:
        search(arr,0,N-1,N//2)
        search(arr,N+1,N+N,N//2)
    
for _ in range(T):
    paper = list(map(int,input()))
    res = 0
    search(paper,0,len(paper)-1,len(paper)//2)
    if res==0:
        print("YES")
    else:
        print("NO")
    


        
        
    
            