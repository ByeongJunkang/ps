n = int(input())
count = 0
for i in range(n):
    dup = list()
    a = list(input())
    isTrue = True
    for j in range(len(a)):
        if a == 0 :
            dup.append(a[0])
        else:
            if a[j] != a[j-1] and a[j] in dup:
                isTrue = False
                break
            else:
                dup.append(a[j])        
    if isTrue == True:
        count +=1
    
    
  
print(count)
    
# N = int(input())
# group_word = N

# for i in range(N) :
#     word = input()
#     for j in range(len(word)-1) :
#         if word[j] == word[j+1] :
#             continue
#         elif word[j] in word[j+1:] :
#             group_word -= 1
#             break
# print(group_word)