X, Y, W, S = map(int,input().split())

cost = 0
if 2 * W <= S:
    cost = X * W + Y * W

else:
    a = min(X,Y)
    if (X + Y) % 2 == 0 and W >= S:
        cost = max(X,Y) * S
    elif (X+Y) %2 ==0 and W<S:
        cost = min(X,Y) * S + abs(X-Y) * W
    elif (X+Y) % 2 == 1 and W >= S:
        cost = (max(X,Y) - 1) * S + W
    else:
        cost = min(X,Y) * S +  abs(X-Y) * W


print(cost)