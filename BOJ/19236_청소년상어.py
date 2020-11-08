from pprint import pprint
di = [0,-1,-1,0,1,1,1,0,-1]
dj = [0,0,-1,-1,-1,0,1,1,1]

# 4x4 보드에 물고기 드가있다. 방향은 8방향
# 청소년 상어가 (0,0) 물고기 먹고 걔 방향과 같아짐
# 물고기 이동 : 번호가 작은 물고기부터 순서대로 이동.
# 빈칸 or 다른 물고기 있음 갈 수 있다.
# 방향이 이동할 수 있는 칸 할 떄까지 45도씩 반시계 회전 , 8번 가면댐
# 딴 물고기 있으면 서로의 위치를 바꾼다.

# 물고기 이동 끝나면 상어가 이동

def pos_fish(num):
    for i in range(4):
        for j in range(4):
            if board[i][j] == []:
                continue
            if board[i][j][0] == num:
                return [i,j,board[i][j][1]]
    return [-1,-1,-1]

def DFS(i,j,dir,cost):
    #print('DFS({},{},{},{})'.format(i,j,dir,cost))
    before = [[-1 for _ in range(4)] for _ in range(4)]
    for ii in range(4):
        for jj in range(4):
            before[ii][jj] = board[ii][jj]
    # 물고기 이동전
    #pprint(before)
    global ans
    if cost > ans:
        ans = cost
    # 물고기 이동
    #pprint(board)
    for num in range(1,17):
        fi,fj,fd = pos_fish(num)
        if [fi,fj,fd] != [-1,-1, -1]:
            for k in range(8):
                nfd = fd+k
                if nfd > 8:
                    nfd -= 8
                nfi,nfj = fi + di[nfd], fj + dj[nfd]
                if nfi < 0 or nfi >= 4 or nfj < 0 or nfj >= 4:
                    continue
                if board[nfi][nfj] == []:
                    if [nfi,nfj] != [i,j]:
                        board[nfi][nfj] = [num,nfd]
                        board[fi][fj] = []
                        break
                elif board[nfi][nfj][0] > 0:
                    temp = board[nfi][nfj]
                    board[nfi][nfj] = [num,nfd]
                    board[fi][fj] = temp
                    break
        #print(num, '물고기 이동 후')
        #pprint(board)
    #print('물고기 전부 이동 후')
    #pprint(board)

    # 상어 이동
    # 상어는 방향에 있는 칸으로 이동, 한번에 여러개의 칸 이동
    # 물고기 있는 칸에 가면 물고기 먹고, 그 방향 가짐
    # 물고기 없는 칸으론 이동할 수 없다. 이동하는 중 지나가는 칸 물고기는 안먹음
    # 물고기 없는 칸으로는 이동할 수 없다.
    k = 1
    while True:
        ni,nj = i + k*di[dir], j + k*dj[dir]

        if ni < 0 or ni >= 4 or nj < 0 or nj >= 4:
            break
        k += 1
        if board[ni][nj] != []:

            fnum = board[ni][nj][0]
            #print(i,j,'에서',ni, nj, fnum, '먹으러감')
            ndir = board[ni][nj][1]
            board[ni][nj] = []
            DFS(ni,nj,ndir,cost+fnum)
            board[ni][nj] = [fnum,ndir]
        # else:
        #     break
    for ii in range(4):
        for jj in range(4):
            board[ii][jj] = before[ii][jj]


board = []
for i in range(4):
    tp = []
    ips = list(map(int,input().split()))
    for j in range(4):
        tp.append([ips[j*2],ips[j*2 + 1]])
    board.append(tp)
#print(board)
# 청소년 상어가 (0,0) 물고기 먹고 걔 방향과 같아짐
snum, sdir = board[0][0]
board[0][0] = []
ans = 0
DFS(0,0,sdir,snum)
print(ans)