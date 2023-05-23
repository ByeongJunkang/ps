a = input()

answer = list()

stack = ''
result = ""
Flag = False
for i in a:
    if Flag == False:
        if i == '<':
            Flag = True
            stack += i
        elif i == ' ':
            stack += i
            result += stack
         
            stack = ""
        else:
            stack = i + stack
    else:
        if i == '>':
            Flag = False
            stack += i
            result += stack
           
            stack=""
        else:
            stack =  stack + i 

            



print(result+stack)
