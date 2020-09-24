ans = 987654321

def validate():
    for i in range(1,N+1):
        end = i
        for j in range(1,H+1):
            if garo[j][end]:
                end += 1
            elif garo[j][end-1]:
                end -= 1
        if i != end:
            return False
    return True

def DFS(cnt,idx):
    global ans
    if cnt > 3 or cnt >= ans:
        return
    if validate():
        if cnt < ans:
            ans = cnt
    for i in range(idx,H+1):
        for j in range(1,N):
            if not garo[i][j] and not garo[i][j-1] and not garo[i][j+1]:
                garo[i][j] = 1
                DFS(cnt+1,i)
                garo[i][j] = 0

N,M,H = list(map(int,input().split()))
garo = [[0 for j in range(100)] for i in range(100)]
for _ in range(M):
    a,b = list(map(int,input().split()))
    garo[a][b] = 1
DFS(0,1)
if ans == 987654321:
    ans = -1
print(ans)