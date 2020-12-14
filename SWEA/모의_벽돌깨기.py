di = [0,0,1,-1]
dj = [1,-1,0,0]

from pprint import pprint

def DFS(idx):
    #print('DFS({})'.format(idx))
    global ans
    if idx == N:
        # 남은 벽돌 개수 ans에 저장
        cnt = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j] != 0:
                    cnt += 1
        if cnt < ans:
            ans = cnt
        return
    for j in range(W):
        # j번 째 열의 맨위 벽돌 터뜨린다.
        # backup 꼭 해야함
        backup = [[-1 for jj in range(W)] for ii in range(H)]
        for ii in range(H):
            for jj in range(W):
                backup[ii][jj] = arr[ii][jj]
        # 벽돌 꺠기
        # BFS로 폭탄 범위에 있는애들 다 방문체크 해주고 큐에 넣음
        # BFS 끝나면 방문 처리 된 애들 다 0으로 만든다
        q = []
        visited = [[False for jj in range(W)] for ii in range(H)]
        for i in range(H):
            if arr[i][j] != 0:
                q.append([i,j])
                visited[i][j] = True
                break
        while q:
            pi,pj = q.pop(0)
            max_range = arr[pi][pj]
            for d in range(4):
                for k in range(1,max_range):
                    ni,nj = pi+k*di[d], pj+k*dj[d]
                    if ni < 0 or nj < 0 or ni >= H or nj >= W:
                        continue
                    if arr[ni][nj] == 0:
                        continue
                    if visited[ni][nj]:
                        continue
                    q.append([ni,nj])
                    visited[ni][nj] = True
        for ii in range(H):
            for jj in range(W):
                if visited[ii][jj]:
                    arr[ii][jj] = 0

        # 위에 떠 있는 벽돌 밑으로 내리기
        for jj in range(W):
            q = []
            for ii in range(H)[::-1]:
                if arr[ii][jj] != 0:
                    q.append(arr[ii][jj])
            for ii in range(H):
                arr[ii][jj] = 0
            id = H-1
            while q:
                p = q.pop(0)
                arr[id][jj] = p
                id -= 1
        #print(j,'번째 벽돌 깬 후')
        #pprint(arr)
        DFS(idx+1)
        for ii in range(H):
            for jj in range(W):
                arr[ii][jj] = backup[ii][jj]


T = int(input())
for tc in range(1,T+1):
    N,W,H = map(int,input().split())
    ans = 987654321
    arr = [list(map(int,input().split())) for i in range(H)]
    DFS(0)
    print('#{} {}'.format(tc,ans))