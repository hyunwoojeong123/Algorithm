di = [0,0,1,-1]
dj = [1,-1,0,0]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    temp_board = [input() for x in range(N)]
    board = []
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(int(temp_board[i][j]))
        board.append(temp)
    visited = [[-1 for j in range(N)] for i in range(N)]
    visited[0][0] = 0
    q = [[0,0]]
    while q:
        i,j = q.pop(0)
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if ni < 0 or nj < 0 or ni >= N or nj >= N:
                continue
            if visited[ni][nj] != -1 and visited[i][j] + board[ni][nj] >= visited[ni][nj]:
                continue
            visited[ni][nj] = visited[i][j] + board[ni][nj]
            q.append([ni,nj])
    print(f'#{tc} {visited[N-1][N-1]}')    
