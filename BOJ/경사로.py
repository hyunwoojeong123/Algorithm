# 1줄 씩 탐색한다.
# 해당 칸에서 DFS돌린다.
def DFS(i,j):
    #print(i,j)
    if j == N-1:
        global ans
        #print('갈 수 있음')
        ans += 1
        return
    # 앞 칸 확인해서 지금 칸이랑 같으면 그 칸으로 이동
    if board[i][j+1] == board[i][j]:
        DFS(i,j+1)
    elif abs(board[i][j+1]-board[i][j]) > 1:
        return
    else:
        # 경사로 놓을 수 있는지 체크
        # 가려는 칸이 지금 칸보다 높은 경우,
        # L만큼 for문돌려서 경사로 건설 가능한지 체크한다. 그리고 tilt도 처리해준다.
        if board[i][j] +1 == board[i][j+1]:
            #뒤로 가면서 체크
            for k in range(L):
                bj = j-k
                #print('{},{} 체크'.format(i, bj))
                if bj < 0:
                    break
                if board[i][bj] != board[i][j]:
                    break
                if tilt[i][bj]:
                    break
            else:
                # 체크했는데, 갈 수있음
                # 경사로 세웟다고 처리해줌.
                for k in range(L):
                    tj = j-k
                    tilt[i][tj] = True
                    #print('{},{} 경사로 세움'.format(i, tj))
                # 담 칸으로 이동함.
                DFS(i,j+1)
        # 가려는 칸이 지금 칸보다 낮은 경우,
        if board[i][j] -1 == board[i][j+1]:
            #앞으로 가면서 체크
            for k in range(1,L+1):
                bj = j+k
                #print('{},{} 체크'.format(i,bj))

                if bj >= N:
                    break
                if board[i][bj] != board[i][j+1]:
                    break
                if tilt[i][bj]:
                    break
            else:
                # 체크했는데, 갈 수있음
                # 경사로 세웟다고 처리해줌.
                for k in range(1,L+1):
                    tj = j+k
                    tilt[i][tj] = True
                    #print('{},{} 경사로 세움'.format(i,tj))
                # 담 칸으로 이동함.
                DFS(i,j+1)

N,L = list(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
board += (list(map(list,zip(*board))))
tilt = [[False for j in range(N)] for i in range(N*2)]
ans = 0
for i in range(N*2):
    #print(board[i])
    DFS(i,0)
print(ans)



