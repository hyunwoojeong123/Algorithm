di = [0,0,1,-1,-1,-1,1,1]
dj = [1,-1,0,0,1,-1,1,-1]

def put(i,j,color):
    #print(f'{i},{j}에 {color} 놓음')
    board[i][j] = color
    opp_color = -1
    if color == 1:
        opp_color = 2
    else:
        opp_color = 1
    for k in range(8):
        ni,nj = i + di[k], j + dj[k]
        flag = False
        cnt = 0
        while ni >= 0 and ni < N and nj >= 0 and nj < N:
            if board[ni][nj] == 0:
                break
            if board[ni][nj] == opp_color:
                cnt += 1
            if board[ni][nj] == color:
                flag = True
                break
            ni += di[k]
            nj += dj[k]
        #print('ni,nj:')
        #print(ni,nj)
        if flag:
            for l in range(1,cnt+1):
                board[i+l*di[k]][j+l*dj[k]] = color


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    board = [[0 for j in range(N)] for i in range(N)]
    board[N//2-1][N//2-1] = 2
    board[N // 2 - 1][N // 2] = 1
    board[N // 2][N // 2 - 1] = 1
    board[N // 2][N // 2] = 2
    for _ in range(M):
        i,j,color = map(int,input().split())
        put(i-1,j-1,color)
        #print(board)
    white,black = 0,0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            if board[i][j] == 2:
                white += 1
    print('#{} {} {}'.format(tc,black,white))