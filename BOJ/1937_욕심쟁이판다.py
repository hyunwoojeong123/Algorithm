import sys
sys.setrecursionlimit(300000)

di = [0,0,1,-1]
dj = [1,-1,0,0]
# i, j 위치에 내렸을 때 처먹을 수잇는 최대 대나무양 리턴
def DFS(i, j):
    # 먼저 4방향 갈수잇느지 없는지 쳌
    pos_dirs = []
    # 갈 수잇는 방향만 따로 배열에 담아놓
    for k in range(4):
        ni,nj = i + di[k], j + dj[k]
        if ni >= 0 and ni < n and nj >= 0 and nj < n and woods[ni][nj] > woods[i][j]:
            pos_dirs.append(k)
    # 암데도 못가면 return
    if len(pos_dirs) == 0:
        return 1
    # D[i][j]값이 -1이아니면 리턴 D[i][j]
    if D[i][j] != -1:
        return D[i][j]
    # 갈수잇는데 잉스면 걔네로 DFS
    for k in pos_dirs:
        ni,nj = i + di[k], j + dj[k]
        temp = 1 + DFS(ni,nj)
        if temp > D[i][j]:
            D[i][j] = temp
    return D[i][j]

n = int(input())
woods = [list(map(int,input().split())) for _ in range(n)]

# 해당 위치에서 최대로 먹을 수 잇는 대나무
D = [[-1 for j in range(n)] for i in range(n)]
ans = -1
for i in range(n):
    for j in range(n):
        ans = max(DFS(i,j),ans)
print(ans)