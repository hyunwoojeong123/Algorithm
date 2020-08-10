import sys
sys.stdin = open("input.txt","r")

N,board = -1,[]
di = [0,0,1,-1]
dj = [1,-1,0,0]
max_len , max_num = -1,-1
def BFS():
    global max_len,max_num
    for i in range(N):
        for j in range(N):
            d = 1
            q = []
            q.append([i,j])
            while q:
                pi,pj = q.pop(0)
                for k in range(4):
                    ni,nj = pi + di[k],pj + dj[k]
                    if ni >= 0 and nj >= 0 and ni < N and nj < N and board[ni][nj] == board[pi][pj] + 1:
                        d += 1
                        q.append([ni,nj])
            if d > max_len:
                max_len = d
                max_num = board[i][j]
            elif d == max_len:
                if max_num > board[i][j]:
                    max_num = board[i][j]



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for x in range(N)]
    max_len, max_num = -1, -1
    BFS()
    print(f'#{tc} {max_num} {max_len}')

