def DFS(idx,g1,g2):
    global ans
    if idx == N:
        if g1 == g2:
            ans = max(ans,g1)
        return
    DFS(idx+1,g1,g2)
    DFS(idx+1,g1+arr[idx],g2)
    DFS(idx+1,g1,g2+arr[idx])

ans = -1
N = int(input())
arr = list(map(int,input().split()))
DFS(0,0,0)
print(ans)