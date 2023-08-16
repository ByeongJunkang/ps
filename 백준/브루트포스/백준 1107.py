# import sys
# sys.setrecursionlimit(10**9)
# N = int(input())
# M = int(input())
# if M ==0:
#     print(len(str(N)))
#     sys.exit()
# if N == 100:
#     print(0)
#     sys.exit()


# broken = list(map(int,input().split()))
# cur = 100
# num = [i for i in range(10)]

# for i in broken:
#     num.remove(i)


# result = []
# min_num = abs(100-N)
# def perm(length):
#     global min_num
#     if len(result) == length:
#         num_str = ''.join(map(str, result))
#         number = int(num_str)
#         min_num = min(min_num,abs(number-N) + length)
#         return
#     for i in range(len(num)):
#         result.append(num[i])
#         perm(length)
#         result.pop()

# for i in range(1,len(str(N))+2):
#     perm(i)
# print(min_num)
import sys
N = int(input())
M = int(input())
if M ==0:
    print(len(str(N)))
    sys.exit()
if N == 100:
    print(0)
    sys.exit()


broken = list(map(int,input().split()))
cur = 100
num = [i for i in range(10)]

for i in broken:
    num.remove(i)
min_num = abs(100-N)
for i in range(1000001):
    
    test = str(i)
    is_num = True
    for j in test:
        if int(j) not in num:
            is_num = False
            break
    
    if is_num:
        min_num = min(min_num,abs(i-N)+len(test),abs(N-i)+len(test))

print(min_num)