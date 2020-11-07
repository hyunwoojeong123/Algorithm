def countSort(arr,n,exp):
    buffer = [-1 for i in range(n)]
    count = [0 for i in range(10)]

    for i in range(n):
        count[(arr[i] / exp) % 10] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    for i in range(0,n)[::-1]:
        buffer[count[(arr[i]/exp) % 10] -1] = arr[i]
        count[(arr[i] / exp) % 10] -= 1
