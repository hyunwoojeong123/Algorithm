# arr = [7,2,3,8,4,5]
# dp = [0 for _ in range(len(arr))]
# for i in range(1,len(dp)):
#     for j in range(i)[::-1]:
#         if arr[i] > arr[j]:
#             if dp[i] < dp[j]+1:
#                 dp[i] = dp[j]+1
#                 break
#             else:
#                 dp[i] = dp[i]
# print(dp)
# print(max(dp))
#

N = int(input())

numList = []

while N > 0:
    a = N % 10
    numList.append(a)
    N = N // 10

if 0 in numList and sum(numList)%3 == 0:
    numList.sort(reverse=True)

    total = 0
    M = len(numList)
    for i in range(M-1):
        total += numList[i]*(10**(M-1-i))
    print(total)

else:
    print(-1)
