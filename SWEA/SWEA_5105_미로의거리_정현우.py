di = [0,0,1,-1]
dj = [1,-1,0,0]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = []
    for i in range(N):
        temp = list(input())
        col = list(map(int,temp))
        board.append(col)
    visited = [[-1 for j in range(N)] for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                q = []
                q.append([i,j])
                visited[i][j] = -1
                while q:
                    tp = q.pop(0)
                    pi,pj = tp[0],tp[1]
                    if board[pi][pj] == 3:
                        ans = visited[pi][pj]
                        break
                    for k in range(4):
                        ni,nj = pi+di[k],pj+dj[k]
                        if ni < 0 or nj < 0 or ni >= N or nj >= N:
                            continue
                        if board[ni][nj] == 1:
                            continue
                        if visited[ni][nj] != -1 and visited[ni][nj] <= visited[pi][pj]+1:
                            continue
                        visited[ni][nj] = visited[pi][pj] + 1
                        q.append([ni,nj])
    print('#{} {}'.format(tc,ans))