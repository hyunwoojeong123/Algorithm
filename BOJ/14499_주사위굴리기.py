# 북
#서 동
# 남

# 주사위 굴릴 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위 바닥에 쓰인 수가 arr로 복사
# 아니면 칸에 쓰인 수가 주사위 바닥으로 복사, 칸은 0이 댄다
# 주사위가 이동했을 때마다 상단에 쓰여 있는 값 출력

di = [-1,0,0,-1,1]
dj = [-1,1,-1,0,0]

# 주사위 인덱스 0 위 1 왼 2 앞 3 오 4 바닥 5 뒤
jusawi = [0,0,0,0,0,0]

def move(dir):
    global x,y
    x += di[dir]
    y += dj[dir]
    if x < 0 or x >= N or y < 0 or y >= M:
        x -= di[dir]
        y -= dj[dir]
        return
    # 주사위 구르기
    new_jusawi = [-1,-1,-1,-1,-1,-1]
    if dir == 1:
        new_jusawi[0] = jusawi[1]
        new_jusawi[1] = jusawi[4]
        new_jusawi[2] = jusawi[2]
        new_jusawi[3] = jusawi[0]
        new_jusawi[4] = jusawi[3]
        new_jusawi[5] = jusawi[5]
    if dir == 2:
        new_jusawi[0] = jusawi[3]
        new_jusawi[1] = jusawi[0]
        new_jusawi[2] = jusawi[2]
        new_jusawi[3] = jusawi[4]
        new_jusawi[4] = jusawi[1]
        new_jusawi[5] = jusawi[5]
    if dir == 3:
        new_jusawi[0] = jusawi[5]
        new_jusawi[1] = jusawi[1]
        new_jusawi[2] = jusawi[0]
        new_jusawi[3] = jusawi[3]
        new_jusawi[4] = jusawi[2]
        new_jusawi[5] = jusawi[4]
    if dir == 4:
        new_jusawi[0] = jusawi[2]
        new_jusawi[1] = jusawi[1]
        new_jusawi[2] = jusawi[4]
        new_jusawi[3] = jusawi[3]
        new_jusawi[4] = jusawi[5]
        new_jusawi[5] = jusawi[0]
    for i in range(6):
        jusawi[i] = new_jusawi[i]
    # arr과 상호작용
    if arr[x][y] == 0:
        arr[x][y] = jusawi[4]
    else:
        jusawi[4] = arr[x][y]
        arr[x][y] = 0
    print(jusawi[0])


N,M,x,y,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dirs = list(map(int,input().split()))
for dir in dirs:
    move(dir)
