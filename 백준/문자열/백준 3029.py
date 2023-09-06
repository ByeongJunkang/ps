a = list(map(int,input().split(":")))
b = list(map(int,input().split(":")))
sec_a = (a[1]) * 60 + a[0] * 3600 + a[2]
sec_b = (b[1]) * 60 + b[0] * 3600 + b[2]
if sec_b <= sec_a:
    sec_b = sec_b + 24 * 3600
ans = sec_b - sec_a
a3=ans//3600
ans%=3600
b3=ans//60
ans%=60
c3=ans
print("%02d:%02d:%02d" %(a3,b3,c3))