#      print(i)

while True:
    b = input()
    if b == "END":
        break
    a = list(b)
    for i in range(len(a)-1,-1,-1):
        print(a[i],end='')
    print("")
# while True:
#     password = input()
#     if password == "END":
#         break
#     else:
#         password = password[::-1]
#         print(password)