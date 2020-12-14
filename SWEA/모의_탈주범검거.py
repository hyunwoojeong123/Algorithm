di = [-1,0,1,0] # 상 우 하 좌
dj = [0,1,0,-1]

dir = [[],[0,1,2,3], [0,2], [1,3], [0,1], [1,2], [2,3], [3,0]]
match = [[1,2,5,6],[1,3,6,7],[1,2,4,7],[1,3,4,5]]

T = int(input())
for tc in range(1,T+1):
    N,M,R,C,L = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0 for j in range(M)] for i in range(N)]
    visited[R][C] = 1
    q = [[R,C]]
    while q:
        i,j = q.pop(0)
        type = arr[i][j]
        for k in dir[type]:
            ni,nj = i+di[k], j+dj[k]
            if ni < 0 or nj < 0 or ni >= N or nj >= M:
                continue
            if visited[ni][nj] > 0:
                continue
            if arr[ni][nj] in match[k]:
                visited[ni][nj] = visited[i][j]+1
                q.append([ni,nj])
    ans = 0
    # print(visited)
    for i in range(N):
        for j in range(M):
            if visited[i][j] > 0 and visited[i][j] <= L:
                ans += 1
    print('#{} {}'.format(tc,ans))