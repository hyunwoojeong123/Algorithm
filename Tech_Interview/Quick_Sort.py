# 안정 정렬 : 동일한 값에 기존 순서가 유지 (버블, 삽입)
# 불안정 정렬 : 동일한 값에 기존 순서가 유지X (선택, 퀵)

def partition(arr,left,right):
    pivot = arr[left]
    i,j = left,right

    while i < j:
        while pivot < arr[j]:
            j -= 1
        while i<j and pivot >= arr[i]:
            i += 1
        arr[i],arr[j] = arr[j],arr[i]
    arr[left] = arr[i]
    arr[i] = pivot

    return i

def quickSort(arr,left,right):
    print('quickSort({},{},{})'.format(arr,left,right))
    if left >= right:
        return
    pi = partition(arr,left,right)

    quickSort(arr,left,pi-1)
    quickSort(arr,pi+1,right)

quickSort([1,3,2,4,5,7,6],0,6)