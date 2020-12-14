di = [-1,0,1,0] # 상우하좌
dj = [0,1,0,-1]

def move(dir):
    global bi,bj,ri,rj
    # 판 기울 때 고려해야할 거
    # 파란 공 먼저 움직이고
    # 빨간 공 먼저 움직임
    # 진행방향에 파란공 or 빨간 공 있는지 확인,
    # 있을 때 없을 때 나눠서 해야대

    # 파란 공
    # print('파공 간다')
    bin,rin = False,False
    way_red = False
    nbi,nbj = bi,bj
    while True:
        nbi,nbj = nbi+di[dir],nbj+dj[dir]
        # print(nbi,nbj)
        if nbi == ri and nbj == rj:
            way_red = True
        if arr[nbi][nbj] == '#':
            nbi -= di[dir]
            nbj -= dj[dir]
            # bi,bj = nbi-di[dir],nbj-dj[dir]
            # if way_red:
            #     bi -= di[dir]
            #     bj -= dj[dir]
            break
        if arr[nbi][nbj] == 'O':
            # bi,bj = nbi,nbj
            bin = True
            break

    # 빨간 공
    # print('빨공 간다')
    way_blue = False
    nri,nrj = ri,rj
    while True:
        nri, nrj = nri + di[dir], nrj + dj[dir]
        # print(nri,nrj)
        if nri == bi and nrj == bj:
            way_blue = True
        if arr[nri][nrj] == '#':
            nri -= di[dir]
            nrj -= dj[dir]
            # ri, rj = nri - di[dir], nrj - dj[dir]
            # if way_blue:
            #     ri -= di[dir]
            #     rj -= dj[dir]
            break
        if arr[nri][nrj] == 'O':
            # print('빨공 드감')
            # ri,rj = nri,nrj
            rin = True
            break
    if rin:
        ri,rj = nri,nrj
    elif way_blue:
        ri,rj = nri-di[dir], nrj-dj[dir]
    else:
        ri,rj = nri,nrj
    if bin:
        bi,bj = nbi,nbj
    elif way_red:
        bi,bj = nbi-di[dir], nbj-dj[dir]
    else:
        bi,bj = nbi,nbj



def DFS(cnt):
    global ans,ri,rj,bi,bj
    # print('DFS({})'.format(cnt))
    # print(ri,rj,bi,bj)

    # visited[ri][rj][bi][bj] = True
    if cnt > 10:
        return
    if cnt >= ans:
        return
    if arr[bi][bj] == 'O':
        return
    if arr[ri][rj] == 'O' and arr[bi][bj] != 'O':
        # print('골인~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        if cnt < ans:
            ans = cnt
        return
    ori,orj,obi,obj = ri,rj,bi,bj
    for k in range(4):
        move(k)
        if not visited[ri][rj][bi][bj]:
            # print('{}방향 이동'.format(k))
            visited[ri][rj][bi][bj] = True
            DFS(cnt+1)
            visited[ri][rj][bi][bj] = False
        ri,rj,bi,bj = ori,orj,obi,obj

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
# print(N,M)
# print(arr)
bi = bj = ri = rj = -1

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'B':
            bi,bj = i,j
            arr[i][j] = '.'
        if arr[i][j] == 'R':
            ri,rj = i,j
            arr[i][j] = ','



ans = 987654321
visited = [[[[False for l in range(M)] for k in range(N)] for j in range(M)] for i in range(N)]
# print(ri,rj,bi,bj)
visited[ri][rj][bi][bj] = True
DFS(0)
# move(3)
# print(ri,rj,bi,bj)
if ans == 987654321:
    ans = -1
print(ans)