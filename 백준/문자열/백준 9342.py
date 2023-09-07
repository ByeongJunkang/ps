t = int(input())

for _ in range(t):
    a = list(input())

    if ord(a[0]) >= ord('G'):
        print("GOOD")
        continue

    first,second,third = 0
    for i in range(a):
        if i == "A" and first == 0:
            first = 1
            continue
        elif i !="A" and first ==0:
            print("GOOD")
            continue
        if first ==1 and second ==0 and third ==0 and a[i] != 'A' and a[i] !="B":


        