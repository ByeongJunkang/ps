a = list(input())
tmp = ''
for i in a:
    if not i.isdigit():
        tmp = tmp + i
b = input()
if b in tmp:
    print(1)
else:
    print(0)
