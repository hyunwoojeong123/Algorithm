di = [0,0,0,-1,1]
dj = [0,1,-1,0,0]

def move(dir):
    global x,y
    #주사위의 위치를 옮긴다.
    nx,ny = x+di[dir],y+dj[dir]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        return
    x,y = nx,ny
    #주사위를 굴린다.
    if dir == 1:
        temp_dice = [-1 for _ in range(6)]
        temp_dice[0] = dice[3]
        temp_dice[1] = dice[1]
        temp_dice[2] = dice[0]
        temp_dice[3] = dice[5]
        temp_dice[4] = dice[4]
        temp_dice[5] = dice[2]
    if dir == 2:
        temp_dice = [-1 for _ in range(6)]
        temp_dice[0] = dice[2]
        temp_dice[1] = dice[1]
        temp_dice[2] = dice[5]
        temp_dice[3] = dice[0]
        temp_dice[4] = dice[4]
        temp_dice[5] = dice[3]
    if dir == 3:
        temp_dice = [-1 for _ in range(6)]
        temp_dice[0] = dice[4]
        temp_dice[1] = dice[0]
        temp_dice[2] = dice[2]
        temp_dice[3] = dice[3]
        temp_dice[4] = dice[5]
        temp_dice[5] = dice[1]
    if dir == 4:
        temp_dice = [-1 for _ in range(6)]
        temp_dice[0] = dice[1]
        temp_dice[1] = dice[5]
        temp_dice[2] = dice[2]
        temp_dice[3] = dice[3]
        temp_dice[4] = dice[0]
        temp_dice[5] = dice[4]
    for i in range(6):
        dice[i] = temp_dice[i]

    #이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰이는 수가 칸에 복사된다.
    if board[x][y] == 0:
        board[x][y] = dice[5]
    #이동한 칸에 쓰여 있는 수가 0이 아니면, 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사된다.
    else:
        dice[5] = board[x][y]
        board[x][y] = 0
    print(dice[0])

N,M,x,y,K = list(map(int,input().split()))
board = [list(map(int,input().split())) for i in range(N)]
dice = [0,0,0,0,0,0]
dirs = list(map(int,input().split()))
for dir in dirs:
    move(dir)
    #주사위의 윗면에 쓰인 수 출력


