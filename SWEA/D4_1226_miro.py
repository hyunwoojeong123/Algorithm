si,sj = -1,-1
di = [0,0,1,-1]
dj = [1,-1,0,0]

for tc in range(1,11):
    t = int(input())
    board = [input() for x in range(16)]
    visited = [[False for j in range(16)] for i in range(16)]
    for i in range(16):
        for j in range(16):
            if board[i][j] == '2':
                si,sj = i,j
                break
    q = []
    q.append([si,sj])
    visited[si][sj] = True
    flag = False
    while q:
        pi,pj = q.pop(0)
        if board[pi][pj] == '3':
            flag = True
            break
        for k in range(4):
            ni,nj = pi + di[k], pj + dj[k]
            if 0 <= ni < 16 and 0 <= nj < 16 and not visited[ni][nj] and board[ni][nj] != '1':
                q.append([ni,nj])
                visited[ni][nj] = True
    if flag:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')