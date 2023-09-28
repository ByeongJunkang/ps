# w = 소문자
# k = 양의 정수
# 어떤 문자를 k개 포함하는 가장 짧은 문자열
# k개 포함하고, 첫 번째 글자와 마지막 글자가 같은, 가장 긴 길이
# from collections import defaultdict
# t = int(input())
# for _ in range(t):
#     letter = list(input())
#     k = int(input())
#     dic = defaultdict(int)
#     start,end = 0
#     dic[letter[start]] +=1
#     while end < len(letter):
#         target = letter[end]
#         if dic[target]: 