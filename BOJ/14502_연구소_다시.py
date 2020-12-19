# 벽을 3개 꼭 세워야함 - 조합
# 그다음 바이러스 퍼뜨린다 - BFs
# 그다음 for문으로 안전영역 크기 구한다음 최대값저장해서 출펵
from pprint import pprint
di = [0,0,1,-1]
dj = [1,-1,0,0]

def make_wall(idx,cnt):
    global ans
    if cnt == 3 or idx >= M*N:
        if cnt == 3:
            # pprint(arr)
            #안전영역 구하기
            q = []
            visited = [[False for j in range(M)] for i in range(N)]
            for i in range(N):
                for j in range(M):
                    if arr[i][j] == 2:
                        q.append([i,j])
                        visited[i][j] = True
            while q:
                pi,pj = q.pop(0)
                for k in range(4):
                    ni,nj = pi+di[k], pj+dj[k]
                    if ni < 0 or ni >= N or nj < 0 or nj >= M:
                        continue
                    if visited[ni][nj]:
                        continue
                    if arr[ni][nj] == 1:
                        continue
                    visited[ni][nj] = True
                    q.append([ni,nj])
            safe = 0
            for i in range(N):
                for j in range(M):
                    if arr[i][j] == 0 and visited[i][j] == False:
                        safe += 1
            # pprint(visited)
            # print(safe)
            if safe > ans:
                ans = safe
        return
    i = idx // M
    j = idx % M
    # print(idx,i,j)
    if arr[i][j] == 0:
        arr[i][j] = 1
        make_wall(idx+1,cnt+1)
        arr[i][j] = 0

    make_wall(idx+1,cnt)

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = -1
make_wall(0,0)
print(ans)