

L, C = map(int,input().split())


Key = dict()
Str = list(input().split())



a = ['a','e','i','o','u']
Str.sort()
def gen_combinations(arr, n):
    result =[] 
    if n == 0: 
        return [[]]

    for i in range(0, len(arr)): 
        elem = arr[i] 
        rest_arr = arr[i + 1:] 
        for C in gen_combinations(rest_arr, n-1): 
            result.append([elem]+C) 
        
   
    return result
        





result = gen_combinations(Str,L)



for i in range(len(result)):
    count = 0
    if 'a' in result[i]:
        Key[i]= True
        continue
    elif 'e' in result[i]:
        Key[i]= True
        continue
    elif 'i' in result[i]:
        Key[i]= True 
        continue

    elif 'o' in result[i]:
        Key[i]= True
        continue
    elif 'u' in result[i]:
        Key[i]= True
        continue
    else:
        Key[i] = False



for i in range(len(result)):
    answer = ''
    if Key[i] == True:
        for j in range(L):
           answer += result[i][j]
    if answer !='':
        print(answer)
 


# import sys

# l, c = map(int, sys.stdin.readline().split())
# words = sorted(list(map(str, sys.stdin.readline().split())))
# answer = []

# def back_tracking(cnt, idx):
#     if cnt == l:
#         vo, co = 0, 0

#         for i in range(l):
#             if answer[i] in ['a', 'e', 'i', 'o', 'u']:
#                 vo += 1
#             else:
#                 co += 1

#         if vo >= 1 and co >= 2:
#             print("".join(answer))

#         return

#     for i in range(idx, c):
#         answer.append(words[i])
#         back_tracking(cnt + 1, i + 1)
#         answer.pop()

# back_tracking(0, 0)