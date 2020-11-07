from collections import deque
from pprint import pprint
di = [0,0,1,-1] # 우,좌,하,상
dj = [1,-1,0,0]

go_dir = {1: [0,1,2,3], 2: [2,3], 3: [0,1], 4: [0,3],
          5: [0,2], 6: [1,2], 7: [1,3]}
next_pipe = {0: [1,3,6,7], 1: [1,3,4,5], 2: [1,2,4,7], 3: [1,2,5,6]}

T = int(input())
for tc in range(1,T+1):
    N,M,R,C,L = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dist = [[0 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append([R,C])
    dist[R][C] = 1
    ans = 0
    while q:
        pi,pj = q.popleft()
        pipe = arr[pi][pj]
        if dist[pi][pj] > L:
            break
        for d in go_dir[pipe]:
            ni,nj = pi+di[d], pj + dj[d]
            if ni < 0 or nj < 0 or ni >= N or nj >= M:
                continue
            if dist[ni][nj] != 0:
                continue
            if arr[ni][nj] in next_pipe[d]:
                dist[ni][nj] = dist[pi][pj]+1
                q.append([ni,nj])
    #print()
    #pprint(dist)
    for i in range(N):
        for j in range(M):
            if dist[i][j] == 0:
                continue
            if dist[i][j] <= L:
                ans += 1
    print('#{} {}'.format(tc,ans))