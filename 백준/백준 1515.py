num_list = list(map(int,input()))
i = 1
while True:
    a = list(map(int,str(i)))
    while len(num_list) > 0 and len(a) > 0:
        if num_list[0] == a[0]:
            del num_list[0]
        del a[0]
    print(i,num_list)
    if len(num_list )== 0:
        break
    i +=1
print(i)


# num_list = list(map(int,input()))
# i = 1
# print(num_list)
# while True:
#     a = list(map(int,str(i)))

#     if len(num_list) >0:
#         for j in range(len(a)):
#             if len(num_list)>0:
#                 if a[j] == num_list[0] and len(num_list) >0:
#                     del num_list[0]
#                     print(i,num_list)
#                 else:
#                     break
#     if len(num_list )== 0:
#         print(i)
#         break
#     i +=1
