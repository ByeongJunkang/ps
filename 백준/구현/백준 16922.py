# I, V, X, L = 1 ,5 ,10, 50
import sys
sys.setrecursionlimit(100000000)
N = int(input())
number = [1,5,10,50]
result = []
result1 = set()
def permutation(num):
    if len(result)== N:
        if sum(result) not in result1:
            result1.add(sum(result))
        return
    
    for i in range(num,4):
        result.append(number[i])
            
        permutation(i)
        result.pop()

permutation(0)
print(len(result1))