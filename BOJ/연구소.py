from pprint import pprint

ans = 0
di = [0,0,1,-1]
dj = [1,-1,0,0]

# 해당 바이러스 퍼뜨리기
def spread(i,j):
    visited[i][j] = True
    board[i][j] = 2
    for dir in range(4):
        ni,nj = i + di[dir],j+dj[dir]
        if ni < 0 or nj < 0 or ni >= N or nj >= M:
            continue
        if board[ni][nj] != 0:
            continue
        if visited[ni][nj]:
            continue
        spread(ni,nj)

# 전체 판 바이러스 퍼뜨리기
def spread_virus():
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2 and not visited[i][j]:
                #print(i,j)
                #print('바이러스 퍼뜨리기')
                spread(i,j)

# 답 갱신 위한 함수
def check():
    global ans
    # 원상복구 위해 복사할 배열
    temp = [[-1 for j in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            temp[i][j] = board[i][j]
    # 바이러스 퍼뜨리기
    spread_virus()
    cnt = 0
    # 바이러스 개수 세기, visited 초기화
    for i in range(N):
        for j in range(M):
            visited[i][j] = False
            if board[i][j] == 0:
                cnt += 1
    # 답 갱신
    if cnt > ans:
        #print(cnt)
        #pprint(board)
        ans = cnt
    # 원상복구
    for i in range(N):
        for j in range(M):
            board[i][j] = temp[i][j]
    return

# 벽 조합으로 세우기
def make_wall(cnt,index):
    if cnt == 3:
        check()
        return

    if index >= N*M:
        return

    make_wall(cnt,index+1)
    i = index // M
    j = index % M
    #print(index,i,j)
    if board[i][j] == 0:
        board[i][j] = 1
        make_wall(cnt+1,index+1)
        board[i][j] = 0

N,M = list(map(int,input().split()))
board = [list(map(int,input().split())) for i in range(N)]
visited = [[False for j in range(M)] for i in range(N)]
make_wall(0,0)
print(ans)