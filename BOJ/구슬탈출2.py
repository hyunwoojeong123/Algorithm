# 공 들의 위치만 기록해서, 걔네들 위치로 DFS를 돌린다.
# 공 움직일 때 고려해야 할 것: 빨간 공 먼저 움직인다. 움직이는 경로에
# 파란 공이나, 벽이 있는지를 고려해야함.

di = [0,0,1,-1]
dj = [1,-1,0,0]
ans = 9999999

def DFS(ri,rj,bi,bj,cnt):
    #print(ri,rj,bi,bj,cnt)
    visited[ri][rj][bi][bj] = cnt
    global ans
    if cnt >= ans or cnt > 10:
        return
    if board[bi][bj] == 'O':
        return
    if board[ri][rj] == 'O':
        #print('{}만에 도착'.format(cnt))
        ans = cnt
    for dir in range(4):
        # 공을 이제 움직인다.
        # 파란 공 먼저 움직인다.
        # 가려는 곳에 벽이나 빨간 공이 있는지 체크한다.
        # 파란 공 위치 구하기
        nbi,nbj = bi+di[dir],bj+dj[dir]
        onway_red = False
        while True:
            if nbi == ri and nbj == rj:
                onway_red = True
            if board[nbi][nbj] == 'O':
                break
            if board[nbi][nbj] == '#':
                nbi -= di[dir]
                nbj -= dj[dir]
                if onway_red:
                    nbi -= di[dir]
                    nbj -= dj[dir]
                break
            nbi += di[dir]
            nbj += dj[dir]
        # 빨간 공 위치 구하기
        nri, nrj = ri + di[dir], rj + dj[dir]
        onway_blue = False
        while True:
            if nri == bi and nrj == bj:
                onway_blue = True
            if board[nri][nrj] == 'O':
                break
            if board[nri][nrj] == '#':
                nri -= di[dir]
                nrj -= dj[dir]
                if onway_blue:
                    nri -= di[dir]
                    nrj -= dj[dir]
                break
            nri += di[dir]
            nrj += dj[dir]
        if visited[nri][nrj][nbi][nbj] > cnt+1:
            DFS(nri,nrj,nbi,nbj,cnt+1)


N, M = map(int,input().split())
board = []
ri,rj,bi,bj = -1,-1,-1,-1
visited = [[[[99999 for l in range(M)] for k in range(N)] for j in range(M)] for i in range(N)]
for i in range(N):
    temp = input()
    col = []
    for char in temp:
        col.append(char)
    board.append(col)
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            board[i][j] = '.'
            ri,rj = i,j
        if board[i][j] == 'B':
            board[i][j] = '.'
            bi,bj = i,j
DFS(ri,rj,bi,bj,0)
if ans == 9999999:
    ans = -1
print(ans)




