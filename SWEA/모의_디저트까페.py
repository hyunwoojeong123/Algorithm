di = [-1,1,1,-1]
dj = [1,1,-1,-1]

def DFS(i,j,cnt, dir):
    global ans
    # print('DFS({},{},{},{})'.format(i,j,cnt,dir))
    visited[i][j] = True
    checked[arr[i][j]] += 1
    ni,nj = i + di[dir],j+dj[dir]
    if ni < 0 or nj < 0 or ni >= N or nj >= N:
        pass
    elif ni == si and nj == sj and dir == 3:
        if ans < cnt+1:
            ans = cnt + 1
    elif checked[arr[ni][nj]]:
        pass
    elif visited[ni][nj]:
        pass
    else:
        DFS(ni,nj,cnt+1,dir)

    if dir != 3:
        ni, nj = i + di[dir+1], j + dj[dir+1]
        if ni < 0 or nj < 0 or ni >= N or nj >= N:
            pass
        elif ni == si and nj == sj and dir+1 == 3:
            # print('씨바라', cnt+1)
            if ans < cnt + 1:
                ans = cnt + 1
        elif checked[arr[ni][nj]]:
            pass
        elif visited[ni][nj]:
            pass
        else:
            DFS(ni, nj, cnt + 1, dir+1)
    visited[i][j] = False
    checked[arr[i][j]] -= 1


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = -1
    visited = [[False for j in range(N)] for i in range(N)]
    checked = [0 for _ in range(101)]
    for i in range(N):
        for j in range(N):
            si,sj = i,j
            # print('si,sj: {},{}'.format(si,sj))
            DFS(i,j,0,0)
    print('#{} {}'.format(tc,ans))