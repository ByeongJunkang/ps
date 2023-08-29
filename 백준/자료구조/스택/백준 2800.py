from itertools import combinations
string = list(input())
ans = 0
real_answer= set()
stack = []
temp = []
for i in range(len(string)):
    if string[i] == "(":
        temp.append(i)
    elif string[i] == ')':
        stack.append([temp.pop(),i])

for i in range(1,len(stack)+1):
    answer = list(combinations(stack,i))
    for num in answer:
        target = list(string)
        for k in num:
            target[k[0]] = ""
            target[k[1]] = ""
        real_answer.add(''.join(target))
        

for ans in sorted(list(real_answer)):
    print(ans)
  