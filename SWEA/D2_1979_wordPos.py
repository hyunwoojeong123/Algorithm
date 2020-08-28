T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]
    visited = [[False for j in range(N)] for i in range(N)]
    ans = 0
    # 0 까만색, 1 흰색
    #가로 체크
    for i in range(N):
        for j in range(N-K+1):
            if board[i][j] == 1 and visited[i][j] == False:
                cnt = 0
                ni,nj = i,j
                while nj < N and board[ni][nj] == 1:
                    visited[ni][nj] = True
                    cnt += 1
                    nj += 1
                if cnt == K:
                    ans += 1
    visited = [[False for j in range(N)] for i in range(N)]
    #세로 체크
    for j in range(N):
        for i in range(N - K + 1):
            if board[i][j] == 1 and visited[i][j] == False:
                cnt = 0
                ni, nj = i, j
                while ni < N and board[ni][nj] == 1:
                    visited[ni][nj] = True
                    cnt += 1
                    ni += 1
                if cnt == K:
                    ans += 1

    print('#{} {}'.format(tc,ans))

