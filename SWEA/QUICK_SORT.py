def partition(arr,left,right):
    pivot = arr[left]
    i,j = left,right
    print('pivot:',pivot)
    print(arr)
    while i < j:
        while pivot < arr[j]:
            j -= 1
        while i < j and pivot >= arr[i]:
            i += 1
        print(i,j,'교환')
        arr[i], arr[j] = arr[j], arr[i]
    arr[left] = arr[i]
    arr[i] = pivot
    print(arr)
    return i

def quickSort(arr, left, right):
    if left >= right:
        return
    print('quicksort(arr,{},{})'.format(left,right))
    pi = partition(arr,left,right)
    print('pi: {}'.format(pi))
    quickSort(arr,left,pi-1)
    quickSort(arr,pi+1,right)

#arr = [11,45,23,81,28,34]
arr = [11,45,22,81,23,34,99,22,17,8]
#arr = [1,1,1,1,1,0,0,0,0,0]
quickSort(arr,0,9)
print(arr)

