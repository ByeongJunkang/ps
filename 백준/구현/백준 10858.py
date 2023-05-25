import sys
N = int(input())

stack = []
for i in range(N):
    order = sys.stdin.readline().rstrip()
    if('push' in order):
        N, M = order.split()
        stack.append(int(M))
    elif('pop' in order):
        if len(stack) > 0:
            print(stack.pop())
        else:
            print('-1')
    elif('top' in order):
        if len(stack) > 0:
            print(stack[-1])
        else:
            print('-1')
    
    elif('empty' in order):
        if len(stack) > 0:
            print(0)
        else:
            print('1')
    elif('size' in order):
        print(len(stack))

        

