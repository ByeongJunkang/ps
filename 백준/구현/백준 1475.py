N = list(map(int,input()))

arr = [0] * 10
for i in N:
    if i == 6:
        if arr[i] != max(arr):
            arr[i]  +=1
        else:
            if arr[9] != max(arr):
                arr[9] +=1
            else:
                arr[i] += 1
    elif i == 9:
        if arr[i] != max(arr):
            arr[i]  +=1
        else:
            if arr[6] != max(arr):
                arr[6] +=1
            else:
                arr[i] += 1
    else:
        arr[i] += 1

print(max(arr))