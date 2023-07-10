import sys
input = sys.stdin.readline
n, m = map(int,input().split())
words = []

words_list = {}

for _ in range(n):
    a = input().rstrip()
    if len(a) >= m:
        if a in words_list:
            words_list[a] +=1
        else:
            words_list[a] = 1

words_list = sorted(words_list.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))

for i in words_list:
    print(i[0])