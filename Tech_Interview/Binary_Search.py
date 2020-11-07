arr = [1,2,3,5,6,7]
def bs(arr,M):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start+end)//2
        print(start,mid,end)
        if M == arr[mid]:
            return mid
        elif M > arr[mid]:
            start = mid+1
        else:
            end = mid-1
    return -1

print(bs(arr,7))
