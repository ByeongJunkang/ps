arr = [i for i in range(10000)]
for i in range(10000):
    a= i % 10000//1000
    b= i % 1000//100
    c= i % 100//10
    d= i % 10//1
    
    num = i + a + b + c + d
    if num in arr:
        arr.remove(num)

for i in arr:
    print(i)