# batch = list(input())
# ans = 0
# stack = []
# razor = 0
# for i in range(len(batch)):
#     if batch[i] == "(":
#         stack.append(batch[i])

#     elif batch[i] == ")":
#         if batch[i-1] == '(':
#             stack.pop()
#             if len(stack) > 0:
#                 razor+= 1
#         elif batch[i-1] != '(':
#             stack.pop()
#             ans += razor + 1
#             if len(stack) == 0:
#                 razor = 0
#     print(stack,razor)
#     print(ans)
# print(ans)



batch = list(input())
ans = 0
stack = []
for i in range(len(batch)):
    if batch[i] == "(":
        stack.append(batch[i])
        ans +=1

    elif batch[i] == ")":
        if batch[i-1] == '(':
            stack.pop()
            ans += len(stack) - 1
        elif batch[i-1] != '(':
            stack.pop()

print(ans)




