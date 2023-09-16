n = int(input())
m = int(input())
letter = input()
tmp = ""
for i in range(n):
    tmp += "IO"
tmp += "I"
ans = 0
count = 0
i = 0
while i < m-1:
    if letter[i:i+3] == "IOI":
        i +=2
        count +=1
        if count == n:
            ans +=1
            count -=1
    else:
        count = 0
        i +=1

print(ans)

 