di = [0,0,1,-1]
dj = [1,-1,0,0]
nums = []

def DFS(i,j):
    global num
    visited[i][j] = 1
    num += 1
    for k in range(4):
        ni,nj = i + di[k],j + dj[k]
        if ni < 0 or nj < 0 or ni >= N or nj >= N:
            continue
        if board[ni][nj] == 0:
            continue
        if visited[ni][nj]:
            continue-=
        DFS(ni,nj)

N = int(input())
board = []
for _ in range(N):
    temp = input()
    col = []
    for char in temp:
        col.append(int(char))
    board.append(col)
visited = [[False for j in range(N)] for i in range(N)]

danji_num = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            num = 0
            DFS(i,j)
            danji_num += 1
            nums.append(num)
            #print(visited)
print(danji_num)
nums = sorted(nums)
for num in nums:
    print(num)