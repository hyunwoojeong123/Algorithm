di = [-1,0,1,0]
dj = [0,1,0,-1]
rev_d = [2,3,0,1]



def operate(i,j,d):
    #print(i,j,d)

    global ans
    #네 방향이 모두 청소가 되어있거나, 벽인 경우

    # 현재 위치 청소
    if not visited[i][j]:
        ans += 1
    visited[i][j] = 1
    # 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행
    # 왼쪽 방향에 아직 청소하지 않은 공간 있으면, 그 방향으로 회전하고 한칸 전진
    nd = (d-1)
    if nd == -1:
        nd = 3
    ni,nj = i+di[nd],j+dj[nd]
    # 왼쪽 방향에 아직 청소하지 않은 공간이 있는경우,
    if board[ni][nj] != 1 and not visited[ni][nj]:
        #print('왼쪽 열려서 왼쪽 방향으로 이동')
        operate(ni,nj,nd)
        return
    # 왼쪽이 막힌 경우
    else:
        # 4방향 체크해서 모두 청소가 되어있거나, 벽인 경우
        cnt = 0
        for k in range(4):
            ki,kj = i+di[k],j+dj[k]
            if board[ki][kj] == 1 or visited[ki][kj]:
                cnt += 1
            else:
                break
        # 4방향 다 막힌 경우,
        if cnt == 4:
            #print('4방향 다 막힘')
            #뒤 방향 확인
            bd = rev_d[d]
            bi,bj = i+di[bd],j+dj[bd]
            #뒤가 벽인 경우
            if board[bi][bj] == 1:
                #print('뒤 막혀서 끝남')
                return
            else:
                #print('뒤로 간다')
                operate(bi,bj,d)
                return
        else:
            operate(i,j,nd)





N,M = list(map(int,input().split()))
i,j,d = list(map(int,input().split()))
board = [list(map(int,input().split())) for i in range(N)]
visited = [[0 for j in range(M)] for i in range(N)]
for ii in range(N):
    for jj in range(M):
        if board[ii][jj] == 1:
            visited[ii][jj] = 1
ans = 0

operate(i,j,d)
print(ans)