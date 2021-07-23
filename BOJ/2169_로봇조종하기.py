import sys
sys.setrecursionlimit(1000001)

di = [0,1,0]
dj = [-1,0,1]

# 0 왼쪽 1 아래 2 오른쪽

def DFS(i,j,before_dir,cost):
    global ans
    cost += arr[i][j]
    if i == N-1 and j == M-1:
        ans = max(ans,cost)
        return
    if D[i][j][before_dir] >= cost:
        return
    D[i][j][before_dir] = cost
    visited[i][j] = True
    for k in range(3):
        ni,nj = i + di[k], j + dj[k]
        if ni < 0 or nj < 0 or ni >= N or nj >= M or visited[ni][nj] or (before_dir != 1 and abs(before_dir-k) == 2):
            continue
        DFS(ni,nj,k,cost)
    visited[i][j] = False

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[False for j in range(M)] for i in range(N)]
D = [[[-1 for k in range(3)] for j in range(M)] for i in range(N)]
ans = -1
DFS(0,0,1,0)
# print(D)
print(ans)
