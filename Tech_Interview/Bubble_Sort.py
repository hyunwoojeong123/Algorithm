arr = [1,3,5,2,4,6,7]
N = len(arr)

for i in range(N):
    for j in range(1,N-i):
        if arr[j-1] > arr[j]:
            arr[j],arr[j-1] = arr[j-1], arr[j]

print(arr)