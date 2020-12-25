def DFS(idx,cnt):
    global ans
    if cnt == N // 2:
        sel = 0
        unsel = 0
        for i in range(N):
            for j in range(i,N):
                if selected[i] and selected[j]:
                    sel += arr[i][j] + arr[j][i]
                if not selected[i] and not selected[j]:
                    unsel += arr[i][j] + arr[j][i]
        diff = abs(sel-unsel)
        if diff < ans:
            ans = diff
        return
    if idx == N:
        return
    selected[idx] = True
    DFS(idx+1,cnt+1)
    selected[idx] = False
    DFS(idx+1,cnt)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 987654321
selected = [False for _ in range(N)]
DFS(0,0)
print(ans)