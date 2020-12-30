from pprint import pprint

# 오 위 왼 아
di = [0,-1,0,1]
dj = [1,0,-1,0]

can_check = [[], [[0],[1],[2],[3]],[[0,2],[1,3]],[[0,1],[1,2],[2,3],[3,0]],[[0,1,2],[1,2,3],[2,3,0],[3,0,1]],[[0,1,2,3]]]

def DFS(idx):
    global ans
    if idx == N*M:
        # 사각지대 개수 세기
        cnt = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0 and not watched[i][j]:
                    cnt += 1
        if ans > cnt:
            # pprint(watched)
            ans = cnt
        return
    pj = idx % M
    pi = idx // M
    # print(i,j)
    if arr[pi][pj] == 0 or arr[pi][pj] == 6:
        DFS(idx+1)
    else:
        type = arr[pi][pj]
        # 6은 벽이라 통과할 수 없다.
        for dirs in can_check[type]:
            backup = [[False for j in range(M)] for i in range(N)]
            for i in range(N):
                for j in range(M):
                    backup[i][j] = watched[i][j]
            for dir in dirs:
                # print(dir,pi,pj,)
                ni,nj = pi+di[dir],pj+dj[dir]
                while True:
                    if ni >= N or nj >= M or ni < 0 or nj < 0 or arr[ni][nj] == 6:
                        break
                    watched[ni][nj] = True
                    ni += di[dir]
                    nj += dj[dir]
            DFS(idx+1)
            for i in range(N):
                for j in range(M):
                    watched[i][j] = backup[i][j]

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
# pprint(arr)
watched = [[False for j in range(M)] for i in range(N)]
ans = 987654321
DFS(0)
print(ans)

