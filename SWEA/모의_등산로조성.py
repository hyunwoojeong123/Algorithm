di = [0,0,1,-1]
dj = [1,-1,0,0]

def DFS(i,j,gongsa,dist):
    global ans
    visited[i][j] = True
    #print(i,j,gongsa,dist)
    if ans < dist:
        ans = dist
    if gongsa == 1:
        for k in range(4):
            ni,nj = i+di[k],j+dj[k]
            if ni < 0 or nj < 0 or ni >= N or nj >= N:
                continue
            if visited[ni][nj]:
                continue
            if board[ni][nj] < board[i][j]:
                DFS(ni,nj,gongsa,dist+1)
            elif abs(board[ni][nj] - board[i][j]) < K:
                backup = board[ni][nj]
                board[ni][nj] = board[i][j]-1
                DFS(ni,nj,0,dist+1)
                board[ni][nj] = backup
    else:
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if ni < 0 or nj < 0 or ni >= N or nj >= N:
                continue
            if visited[ni][nj]:
                continue
            if board[ni][nj] < board[i][j]:
                DFS(ni, nj, gongsa, dist + 1)
    visited[i][j] = False

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]
    visited = [[False for j in range(N)] for i in range(N)]
    mh = -1
    for i in range(N):
        for j in range(N):
           if mh < board[i][j]:
               mh = board[i][j]
    ans = 0
    for i in range(N):
        for j in range(N):
            if mh == board[i][j]:
                DFS(i,j,1,1)
    print('#{} {}'.format(tc,ans))