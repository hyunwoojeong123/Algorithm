T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    board = []
    for i in range(N):
        board.append(list(map(int,input().split())))
    ans = -1
    for i in range(0,N-M+1):
        for j in range(0,N-M+1):
            killed = 0
            for k in range(0,M):
                for l in range(0,M):
                    killed += board[i+k][j+l]
            ans = max(ans,killed)
    print(f'#{tc} {ans}')