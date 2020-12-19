di = [-1,0,1,0]
dj = [0,1,0,-1]
back_d = [2,3,0,1]

N,M = map(int,input().split())
i,j,d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[False for j in range(M)] for i in range(N)]

while True:
    visited[i][j] = True
    cnt = 0
    nd = d
    for _ in range(1,5):
        nd -= 1
        if nd == -1:
            nd = 3
        # 해당 방향에 청소안한애가 있는지 체크
        ni,nj = i+di[nd],j+dj[nd]
        if arr[ni][nj] == 0 and not visited[ni][nj]:
            i,j,d = ni,nj,nd
            break
        else:
            cnt+= 1
    if cnt == 4:
        bd = back_d[d]
        bi,bj = i+di[bd],j+dj[bd]
        if arr[bi][bj] == 1:
            break
        else:
            i,j = bi,bj

ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j]:
            ans += 1
# from pprint import pprint
# pprint(visited)
print(ans)



