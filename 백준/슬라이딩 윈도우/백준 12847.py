n,m = map(int,input().split())
money = list(map(int,input().split()))
benefit = sum(money[:m])
answer =benefit
for i in range(m,n):
    benefit += money[i] - money[i-m]
    answer = max(answer,benefit)
print(answer)