arr = [1,3,2,4,5,7,6]
N = len(arr)
# Bubble sort
# 계속 비교하면서 바꾸서 맨 마지막부터 정렬된 값이 채워진다. O(N**2)
# for i in range(N):
#     for j in range(1,N-i):
#         if arr[j-1] > arr[j]:
#             arr[j],arr[j-1] = arr[j-1],arr[j]
# print(arr)

# Insertion sort
# 2번째 인덱스부터 해당 값이 배열의 해당 인덱스 앞 에서 몇번째 위치인지 찾는다.
# 찾는거는 인덱스의 전부터 0으로 쭉 가는데, 걔보다 작은 값이면 멈춘다.
# 한칸씩 미는 느낌
for i in range(2,N):
    temp = arr[i]
    prev = i-1
    while prev >= 0 and arr[prev] > temp:
        arr[prev+1] = arr[prev]
        prev -= 1
    arr[prev+1] = temp

print(arr)

# Selection sort
# 최소값 찾아서 맨 앞부터 차례대로 채운다.
# 게속 비교를 안하기 때문에 Bubble보다는 빠름 O(N**2)
# for i in range(N):
#     idx = i
#     for j in range(i,N):
#         if arr[j] < arr[idx]:
#             idx = j
#     arr[i],arr[idx] = arr[idx],arr[i]
#
# print(arr)
