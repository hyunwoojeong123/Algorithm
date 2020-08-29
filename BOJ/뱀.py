dir_changes = []
di = [0,1,0,-1]
dj = [1,0,-1,0]


N = int(input())
board = [[0 for j in range(N)] for i in range(N)]

K = int(input())
for _ in range(K):
    i,j = map(int,input().split())
    board[i-1][j-1] = 1

L = int(input())
for _ in range(L):
    temp = input().split()
    X,C = int(temp[0]), temp[1]
    dir_changes.append((X,C))

dir_changes_start_index = 0
#print(dir_changes)
t = 0
snake = [[0,0]]
dir = 0
while True:
    t += 1
    #대가리를 다음 칸에 둔다.
    hi,hj = snake[len(snake)-1]
    nhi,nhj = hi+di[dir], hj+dj[dir]
    #움직이기 전에 충돌 확인을 함
    #벽에 부디면, 종료
    if nhi < 0 or nhi >= N or nhj < 0 or nhj >= N:
        break
    #자기 자신의 몸과 부디면, 종료
    if [nhi,nhj] in snake:
        break
    snake.append([nhi,nhj])
    # 이동한 칸에 사과가 있으면,
    if board[nhi][nhj]:
        board[nhi][nhj] = 0
    # 이동한 칸에 사과가 없으면,
    else:
        snake.pop(0)
    if dir_changes_start_index < L and t == dir_changes[dir_changes_start_index][0]:
        if dir_changes[dir_changes_start_index][1] == 'D':
            dir += 1
            if dir >= 4:
                dir = 0
        else:
            dir -= 1
            if dir < 0:
                dir = 3
        dir_changes_start_index += 1
    #print(t,snake)
    #print('{}로 바꿈'.format(dir))
print(t)