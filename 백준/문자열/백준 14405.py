s = input().replace("pi","P").replace("ka","K").replace("chu","C")
pika = True
for i in s:
    if i =="P" or i =="K" or i =="C":
        continue
    else:
        pika= False
        break

if pika:
    print("YES")
else:
    print("NO")