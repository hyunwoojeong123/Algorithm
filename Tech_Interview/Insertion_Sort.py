arr = [1,3,2,4,5,7,6]
N = len(arr)
for i in range(N-1):
    idx  = i
    for j in range(i+1,N):
        if arr[j] < arr[idx]:
            idx = j

    arr[i],arr[idx] = arr[idx],arr[i]

print(arr)