arr = [1,3,2,4,5,7,6]
N = len(arr)
for i in range(N):
    min_val,min_idx = arr[i],i
    for j in range(i,N):
        if min_val > arr[j]:
            min_val, min_idx = arr[j],j

    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    #print(arr)

print(arr)

