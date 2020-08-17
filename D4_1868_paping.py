di = [-1,-1,-1,0,1,1,1,0]
dj = [-1,0,1,1,1,0,-1,-1]

# num 배열에 주변 지뢰의 숫자를 기입한다.
# check배열로 0의 위치들을 먼저 체크해서 주변을 check로 만들어주고, 겹치면
# 겹치는대로 더해서, cnt에 1을 더한다.
# 나머지 check 안채워진 부분들 중에 지뢰가 심어져 있지 않은 곳의 개수만큼 cnt에 더해 준다.

num = []

def makeNum(board):
    num = []
    for i in range(N):
        temp = []
        for j in range(N):
            if board[i][j] == '*':
                temp.append(-1)
                continue
            sum = 0
            for k in range(8):
                ni,nj = i + di[k], j + dj[k]
                if ni < 0 or nj < 0 or ni >= N or nj >= N:
                    continue
                if board[ni][nj] == '*':
                    sum += 1
            temp.append(sum)
        num.append(temp)
    return num

def zerocheck(i,j,visited):
    if visited[i][j] == False:
        visited[i][j] = True
        for k in range(8):
            ni,nj = i + di[k], j + dj[k]
            if ni < 0 or nj < 0 or ni >= N or nj >= N:
                continue
            if num[ni][nj] == 0:
                zerocheck(ni,nj,visited)
            visited[ni][nj] = True
            

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [input() for x in range(N)]
    num = makeNum(board)
    #print(board,num)
    visited = [[False for j in range(N)] for i in range(N)]
    zero_pos = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == '*':
                visited[i][j] = True
            if num[i][j] == 0:
                zero_pos.append([i,j])
    cnt = 0
    while len(zero_pos) > 0:
        pi,pj = zero_pos.pop(0)
        if visited[pi][pj] == False:
            zerocheck(pi,pj,visited)
            cnt += 1
    for i in range(N):
        for j in range(N): 
            if visited[i][j]:
                continue
            cnt+= 1
    print(f'#{tc} {cnt}')
            

