# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None


# class LinkedList:

#     def __init__(self,data):
#         self.head = Node(data)
    


        
import sys
input = sys.stdin.readline
word = list(input().rstrip())
M = int(input())
result = []
for _ in range(M):
    answer = input().split()
    if answer[0] == "L":
        if len(word) >0:
            result.append(word.pop())
    elif answer[0] == "D":
        if len(result) >0:
            word.append(result.pop())
    
    elif answer[0] == "P":
        word.append(answer[1])

    elif answer[0] == "B":
        if len(word)>0:
            word.pop()

word.extend(list(reversed(result)))
for i in word:
    print(i,end="")

    
















#     if i == len(word)-1:
#         continue
#     Node(word[i]).next = Node(word[i+1])

# print(Node)
# print(Node("a")