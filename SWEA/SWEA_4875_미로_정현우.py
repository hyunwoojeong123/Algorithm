di = [0,0,1,-1]
dj = [1,-1,0,0]

def DFS(i,j):
    visited[i][j] = True
    if board[i][j] == 3:
        global ans
        ans = 1
    for k in range(4):
        ni,nj = i + di[k],j + dj[k]
        if ni < 0 or nj < 0 or ni >= N or nj >= N:
            continue
        if visited[ni][nj]:
            continue
        if board[ni][nj] == 1:
            continue
        DFS(ni,nj)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = []
    visited = [[False for j in range(N)]for i in range(N)]
    ans = 0
    for _ in range(N):
        temp = input()
        col = []
        for each in temp:
            col.append(int(each))
        board.append(col)
    si,sj = -1,-1
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                si,sj = i,j
    DFS(si,sj)
    print('#{} {}'.format(tc,ans))