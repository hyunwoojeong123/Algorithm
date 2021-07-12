di = [0,0,1,-1]
dj = [1,-1,0,0]
N,L,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
while True:
    moved = False
    mass = 1
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()

    included = [[0 for jjj in range(N)] for iii in range(N)]
    mass = 1

    for ii in range(N):
        for jj in range(N):
            # print(ii,jj,'검사')

            q = [[ii,jj]]
            SUM = arr[ii][jj]
            CNT = 1
            while q:
                pi,pj = q.pop(0)
                # print(pi,pj,'방문')
                for k in range(4):
                    ni,nj = pi+di[k],pj+dj[k]
                    if ni < 0 or nj < 0 or ni >= N or nj >= N:
                        continue
                    if included[ni][nj]:
                        continue
                    if abs(arr[ni][nj] - arr[pi][pj]) >= L and abs(arr[ni][nj] - arr[pi][pj]) <= R:
                        included[ni][nj] = True
                        q.append([ni,nj])
                        SUM += arr[ni][nj]
                        CNT += 1
            if CNT > 1:
                moved = True
            avg = SUM // CNT
            for iiii in range(N):
                for jjjj in range(N):
                    if included[iiii][jjjj]:
                        arr[iiii][jjjj] = avg
    if not moved:
        break
    else:
        cnt += 1

print(cnt)