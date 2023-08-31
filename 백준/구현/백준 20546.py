Money = int(input())
cost = list(map(int,input().split()))

jun_money = Money
jun_stock = 0
jun_resource = 0
for i in range(14):
    if jun_money > 0:
        if jun_money // cost[i] >0:
            temp = jun_money // cost[i]
            jun_stock = jun_money // cost[i] + jun_stock
            jun_money = jun_money -temp * cost[i]
jun_resource = jun_stock * cost[-1] + jun_money


sung_money = Money
sung_stock = 0
sung_resource = 0

is_increase = 0
is_decrease = 0
for i in range(1,14):
    if cost[i-1] < cost[i]:
        is_increase +=1
        is_decrease = 0
    elif cost[i-1] > cost[i]:
        is_decrease +=1
        is_increase = 0
    elif cost[i-1] == cost[i]:
        is_increase = 0
        is_decrease = 0

    if is_decrease >= 3:
        if sung_money // cost[i] >0:
            temp = sung_money // cost[i]
            sung_stock = sung_stock +sung_money // cost[i]
            sung_money = sung_money - temp * cost[i]
    elif is_increase == 3:
        sung_resource = cost[i] * sung_stock + sung_resource + sung_money
        sung_stock = 0
    

if sung_stock > 0:
    sung_resource = cost[-1] * sung_stock + sung_money

elif sung_stock == 0 and sung_resource ==0:
    sung_resource = Money

if sung_resource == jun_resource:
    print("SAMESAME")
elif sung_resource > jun_resource:
    print("TIMING")
else:
    print("BNP")

