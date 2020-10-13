from pprint import pprint

N,M,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
di = [0,-1,1,0,0]
dj = [0,0,0,-1,1]
dir = list(map(int,input().split()))
dir = [-1] + dir
prior = [[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]]
for i in range(M):
    tp = [[0,0,0,0]]
    for j in range(4):
        tptp = list(map(int,input().split()))
        tp.append(tptp)
    prior.append(tp)

# 상어 위치를 다 pos에 담는다.
pos = [[] for _ in range(M+1)]
dead = [False for _ in range(M+1)]
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            pos[board[i][j]] = [i,j]
# 상어 살아있는 개수
alive = M
#print('alive', alive)
# 상어 냄새 사라지는 시간
t_left = [[-1 for j in range(N)] for i in range(N)]
# 상어 냄새
stink = [[0 for j in range(N)] for i in range(N)]
for i in range(1,M+1):
    ii,jj = pos[i]
    stink[ii][jj] = i
    t_left[ii][jj] = K 

# 시뮬
t = 0
while t <= 1000:
    #print(t, '상태')
    #pprint(stink)
    #pprint(t_left)
    #print(pos)
    #print(alive)
    # 상어 이동
    for shark in range(1,M+1):
        # 상어가 죽었으면, 넘어감
        if dead[shark]:
            continue
        ## 인접한 칸 중 아무 냄새 없는 칸 찾음. 도는 순서는 우선순위대로
        si,sj = pos[shark]
        moved = False
        for d in prior[shark][dir[shark]]:
            nsi,nsj = si + di[d], sj + dj[d]
            # 격자 밖으로는 못나감
            if nsi < 0 or nsi >= N or nsj < 0 or nsj >= N:
                continue
            # 냄새 없으면, 걸로 이동
            if stink[nsi][nsj] == 0:
                pos[shark] = nsi,nsj
                moved = True
                dir[shark] = d
                break
        if moved:
            continue
        ## 인접한 칸 중 지 냄새 있는 곳 찾음.
        for d in prior[shark][dir[shark]]:
            nsi,nsj = si + di[d], sj + dj[d]
            # 격자 밖으로는 못나감
            if nsi < 0 or nsi >= N or nsj < 0 or nsj >= N:
                continue
            # 지 냄새면, 걸로 이동
            if stink[nsi][nsj] == shark:
                pos[shark] = nsi,nsj
                moved = True
                dir[shark] = d
                break
    t += 1
    # 상어끼리 잡아먹기
    for i in range(1,M+1):
        if dead[i]:
            continue
        for j in range(i+1,M+1):
            if dead[j]:
                continue
            if pos[i] == pos[j]:
                dead[j] = True
                alive -= 1
                pos[j] = [-1,-1]
    # 상어 한개만 남으면 겜 긑낸다
    if alive == 1:
        break
    # 냄새 뿌리기
    for shk in range(1,M+1):
        if dead[shk]:
            continue
        ii,jj = pos[shk]
        stink[ii][jj] = shk 
        # t_left에 냄새 사라지는 시간 기록
        t_left[ii][jj] = t+K
    # 없어질 냄새 처리
    for ii in range(N):
        for jj in range(N):
            if t_left[ii][jj] == t and stink[ii][jj] != 0:
                t_left[ii][jj] = -1
                stink[ii][jj] = 0
if t > 1000:
    t = -1
print(t)
