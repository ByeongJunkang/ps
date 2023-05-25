a = input()

list = [0] * 8
list[0] =  "c="
list[1] = "c-"
list[2] = "dz="
list[3] = "d-"
list[4] = "lj"
list[5] = "nj"
list[6] = "s="
list[7] = "z="


for i in list:
    a = a.replace(i,"*")

print(len(a))


    
    


