di = [0,1,0,-1] # 오,아,왼,위
dj = [1,0,-1,0]
board = []
N = -1

def paint(i,j,dir,num):
    #print(i,j,dir,num)
    global board
    board[i][j] = num
    #print(board)
    ni,nj = i+di[dir],j+dj[dir]
    if num == N*N:
        return
    if ni < 0 or nj < 0 or ni >= N or nj >= N or board[ni][nj] != -1:
        paint(i,j,(dir+1) % 4,num)
    else:
        paint(ni,nj, dir,num+1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [[-1 for j in range(N)] for i in range(N)]
    paint(0,0,0,1)
    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = ' ')
        print()
