from collections import deque

N, K = map(int,input().split())
queue = deque()
answer = list()
for i in range(1,N+1):
    queue.append(i)

for i in range(len(queue)):
    queue.rotate(-K)
    answer.append(queue.pop())

formatted_list = "<{}>".format(", ".join(str(i) for i in answer))
print(formatted_list)
