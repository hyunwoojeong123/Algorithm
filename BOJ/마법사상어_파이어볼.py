di = [-1,-1,0,1,1,1,0,-1]
dj = [0,1,1,1,0,-1,-1,-1]

N,M,K = map(int,input().split())
board = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r,c,m,s,d = map(int,input().split())
    board[r-1][c-1].append([m,s,d])

for _ in range(K):
    temp = [[[] for _ in range(N)] for _ in range(N)]
    # 파이어볼 이동
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                while board[i][j]:
                    m,s,d = board[i][j].pop()
                    ni,nj = (i+s*di[d])%N,(j+s*dj[d])%N
                    temp[ni][nj].append([m,s,d])
    # 파이어볼 합치기
    for i in range(N):
        for j in range(N):
            if len(temp[i][j]) >= 2:
                tot_cnt = len(temp[i][j])
                total_m = 0
                total_s = 0
                holsu_cnt = 0
                while temp[i][j]:
                    m,s,d = temp[i][j].pop()
                    total_m += m
                    total_s += s
                    if d % 2 == 1:
                        holsu_cnt += 1
                total_m = total_m//5
                total_s = total_s//tot_cnt
                if total_m > 0:
                    if holsu_cnt == tot_cnt or holsu_cnt == 0:
                        for k in [0,2,4,6]:
                            temp[i][j].append([total_m,total_s,k])
                    else:
                        for k in [1,3,5,7]:
                            temp[i][j].append([total_m, total_s, k])
    for i in range(N):
        for j in range(N):
            board[i][j] = temp[i][j]

ans = 0
for i in range(N):
    for j in range(N):
        if board[i][j]:
            for each in board[i][j]:
                ans += each[0]
print(ans)