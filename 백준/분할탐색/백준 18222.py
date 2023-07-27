k = int(input())

def recursion(k):
    if k == 0:
        return 0
    
    elif k ==1:
        return 1
    
    elif k%2:
        return 1 - recursion(k//2)
    else:
        return recursion(k//2)
    
print(recursion(k-1))