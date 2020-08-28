import sys
sys.stdin = open("input.txt","r")

board, visited = [],[]
di = [0,0,-1,1] # 오,왼,아,위
dj = [1,-1,0,0]

def find_startX(i,j):
    #print(i,j)
    visited[i][j] = True
    if i == -1 and j == -1:
        return -1
    if i == 0:
        return j
    # 길 찾는 법. 양 옆을 먼저 본다.
    for k in range(3):
        ni,nj = i+di[k],j+dj[k]
        # 벽을 나갓거나 0이면 continue
        if ni < 0 or nj < 0 or ni >= 100 or nj >= 100:
            continue
        elif board[ni][nj] == 0 or visited[ni][nj] == True:
            continue
        else:
            return find_startX(ni,nj)
            break


for tc in range(1,11):
    tnum = int(input())
    board = []
    e_i,e_j = -1,-1
    for i in range(100):
        temp = list(map(int,input().split()))
        board.append(temp)
        for j in range(100):
            if temp[j] == 2:
                e_i,e_j = i,j
    visited = [[False for j in range(100)]for i in range(100)]
    print(f'#{tc} {find_startX(e_i,e_j)}')
