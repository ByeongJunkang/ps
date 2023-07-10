N =int(input())
word_list = []
for _ in range(N):
    word_list.append(input())

a = list(word_list.pop(0))
count = 0
for i in word_list:
    temp = a[:]
    num = len(a)
    i_list = list(i)
    for j in i_list:
        if j in temp:
            num -=1
            temp.remove(j)
            
    if num == 0 and len(i) == len(a) :
        count+=1
    elif num == 1 and len(i) == len(a)-1:
        count+=1 
    elif num == 1 and len(i) == len(a):
        count+=1
    elif num == 0 and len(i) == len(a) + 1:
        count+=1
print(count)
