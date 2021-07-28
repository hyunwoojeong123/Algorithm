def DFS(idx,diff):
    if diff > 250000:
        return IMPOSSIBLE
    if idx == N:
        if diff == 0:
            return 0
        else:
            return IMPOSSIBLE
    if D[idx][diff] != -1:
        return D[idx][diff]
    # diff는 높은 거 - 낮은 거
    # 높이는 낮은거 기준
    # 블럭 사용안함
    D[idx][diff] = IMPOSSIBLE
    D[idx][diff] = max(DFS(idx+1,diff),D[idx][diff])
    # 낮은쪽에 쌓음
        # diff보다 블럭이 크면
    if diff < arr[idx]:
        D[idx][diff] = max(DFS(idx+1,-diff+arr[idx])+diff,D[idx][diff])
        # diff보다 블럭이 작으면
    else:
        D[idx][diff] = max(DFS(idx+1,diff-arr[idx])+arr[idx],D[idx][diff])
    # 높은쪽에 쌓음
    D[idx][diff] = max(DFS(idx+1,diff+arr[idx]),D[idx][diff])
    return D[idx][diff]

IMPOSSIBLE = -987654321

N = int(input())
arr = list(map(int,input().split()))
D = [[-1 for _ in range(500005)] for _ in range(N+2)]
ans = DFS(0,0)
# print(ans)
if ans == 0:
    print(-1)
else:
    print(ans)

