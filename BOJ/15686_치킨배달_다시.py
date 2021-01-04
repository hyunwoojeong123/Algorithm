
def BFS(i,j):
    dist = 987654321
    for ii in range(len(chickens)):
        ci,cj = chickens[ii]
        if selected[ii]:
            td = abs(i-ci) + abs(j-cj)
            if td < dist:
                dist = td
    return dist


def DFS(idx,cnt):
    global ans
    if cnt == M:
        tp = 0
        for (i,j) in homes:
            tp += BFS(i,j)
        if tp < ans:
            ans = tp
        return
    for ii in range(idx,len(chickens)):
        if selected[ii]:
            continue
        selected[ii] = True
        DFS(ii,cnt+1)
        selected[ii] = False

N,M = map(int,input().split())
homes = []
chickens = []
arr = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            homes.append([i,j])
        if arr[i][j] == 2:
            chickens.append([i,j])
ans = 987654321
selected = [False for _ in range(len(chickens))]
# 치킨집 M개를 골른다.
DFS(0,0)
print(ans)
