# 우하좌상
di = [0,1,0,-1]
dj = [1,0,-1,0]

N = int(input())
K = int(input())
arr = [[False for j in range(N)] for i in range(N)]
for _ in range(K):
    i,j = map(int,input().split())
    i -= 1
    j -= 1
    arr[i][j] = True
L = int(input())
changes = dict()
for _ in range(L):
    X,C = input().split()
    X = int(X)
    changes[X] = C

t = 0
dir = 0
snake = [[0,0]]
while True:
    t += 1
    sh = snake[len(snake)-1]
    st = snake[0]
    nh = [sh[0] + di[dir], sh[1] + dj[dir]]
    # print(nh, '로 가려 함')
    if nh in snake or nh[0] < 0 or nh[0] >= N or nh[1] < 0 or nh[1] >= N:
        break
    snake.append(nh)
    if arr[nh[0]][nh[1]]:
        arr[nh[0]][nh[1]] = False
    else:
        snake.pop(0)
    # print(t, snake, dir)
    change = changes.get(t, 0)
    if change != 0:
        if change == 'L':
            dir -= 1
            if dir == -1:
                dir = 3
        else:
            dir += 1
            if dir == 4:
                dir = 0
print(t)


