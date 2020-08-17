T = int(input())
for tc in range(1,T+1):
    N,M = list(map(int,input().split()))
    linked = [[False for j in range(N+1)] for i in range(N+1)]
    for i in range(M):
        x,y = list(map(int,input().split()))
        linked[x][y] = True
        linked[y][x] = True
    #print(linked)
    ans = 0
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            for k in range(j+1,N+1):
                if linked[i][j] and linked[j][k] and linked[k][i]:
                    ans += 1
    print(f'#{tc} {ans}')
