s = list(map(str,input()))
length = len(s)


kk = 0 
Pelindrum = False            
for i in range(length-1):
     Pelindrum = False
     count = 0
     if s[i] == s[length-1]:
          j = 1
          k = i
          while k <= (length -j):
               if s[k] == s[length-j]:
                    Pelindrum = True
     
               else:
                    Pelindrum = False
                    break
               count +=1
               k+=1
               j+=1
     if Pelindrum == True:
         kk = i
         break


if Pelindrum == False and kk == 0:
     print(length*2-1)
elif Pelindrum == True and kk == 0:
     print(length)
elif Pelindrum == True and kk != 0:
     print(length+kk)

               

          







