def find(n):
    if n < 2:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
        while result % 10 == 0:
            result //= 10
    return result % 10

n = int(input())
result = find(n)
print(result)
