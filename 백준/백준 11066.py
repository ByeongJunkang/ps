import heapq
n = int(input())

for _ in range(n):
    tmp  =0
    num = int(input())
    q = list(map(int,input().split()))
    heapq.heapify(q)
    while q:
        if len(q) >=2:
            a = heapq.heappop(q)
            b = heapq.heappop(q)
            tmp +=(a+b)
            heapq.heappush(q,a+b)
        if len(q) == 1:
            a = heapq.heappop(q)

        print(q,tmp)
    
            # tmp +=a
    
    print(tmp)

