

ans = -1
di = [0,0,1,-1]
dj = [1,-1,0,0]
yut_di = [[-1,0,1,0],[0,1,0,0],[-1,0,1,0],[0,-1,0,0]]
yut_dj = [[0,0,0,1],[-1,0,0,1],[0,0,0,-1],[-1,0,0,1]]

def DFS(i,j,cnt,hab):
    global ans
    visited[i][j] = True
    hab += board[i][j]
    if hab + (4-cnt)*max_n <= ans:
        return
    if cnt == 4:
        #print(hab)
        if ans < hab:
            ans = hab
        return
    # 엿모양 체크
    for k in range(4):
        yut_hab = 0
        for l in range(4):
            yi,yj = i + yut_di[k][l],j + yut_dj[k][l]
            if yi < 0 or yi >= N or yj < 0 or yj >= M:
                break
            yut_hab += board[yi][yj]
        else:
            if ans < yut_hab:
                ans = yut_hab

    for dir in range(4):
        ni,nj = i+di[dir],j+dj[dir]
        if ni < 0 or nj < 0 or ni >= N or nj >= M:
            continue
        if visited[ni][nj]:
            continue
        DFS(ni,nj,cnt+1,hab)
        visited[ni][nj] = False

N,M = list(map(int,input().split()))
board = [list(map(int,input().split())) for i in range(N)]
visited = [[False for j in range(M)] for i in range(N)]

max_n = -1
#max 값 찾기.
for i in range(N):
    for j in range(M):
        if board[i][j] > max_n:
            max_n = board[i][j]

for i in range(N):
    for j in range(M):
        DFS(i,j,1,0)
        visited[i][j] = False


print(ans)
