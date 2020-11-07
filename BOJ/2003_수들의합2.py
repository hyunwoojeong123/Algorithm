N, M = map(int,input().split())
arr = list(map(int,input().split()))
start = end = hab = ans = 0

while True:
    if hab == M:
        #print(start,end)
        ans += 1

    if hab >= M:
        hab -= arr[start]
        start += 1
    elif end == N:
        break
    elif hab < M:
        hab += arr[end]
        end += 1


print(ans)