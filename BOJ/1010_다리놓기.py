r, c = map(int, input().split())
dx = [-1, 0, 1]
dy = [1, 1, 1]

arr = [list(input()) for _ in range(r)]
visit = [[0]*c for _ in range(r)]
flag = False
cnt = 0
def dfs(x, y):
    global cnt,flag
    visit[x][y] = 1
    if y == c-1:
        flag = True
        cnt += 1
        return

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= r or ny >= c or visit[nx][ny] == 1 or arr[nx][ny] == 'x':
            continue
        dfs(nx,ny)
        if flag:
            return

for i in range(r):
    flag = False
    dfs(i, 0)
print(cnt)