def merge(array,left,mid,right):
    print('merge(arr,{},{},{})'.format(left,mid,right))
    L,R = [],[]
    for i in range(left,mid+1):
        L.append(array[i])
    for i in range(mid+1,right+1):
        R.append(array[i])
    i,j,k = 0,0,left
    ll,rl = len(L),len(R)
    while i < ll and j < rl:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    while i < ll:
        array[k] = L[i]
        k += 1
        i += 1
    while j < rl:
        array[k] = R[j]
        k += 1
        j += 1

def mergeSort(array,left,right):
    if left < right:
        print('mergeSort(arr,{},{})'.format(left,right))
        mid = (left + right) // 2

        mergeSort(array,left,mid)
        mergeSort(array,mid+1,right)
        merge(array,left,mid,right)

arr = [5,4,3,2,1]
mergeSort(arr,0,4)
print(arr)

# 머지소트 호출 순서
# f  L R mid
# ms 0 6 3
#  0 3
# ms 0 1
# 2 3
# 4 6