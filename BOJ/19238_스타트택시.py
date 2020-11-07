# 특정 위치로 이동할 때 항상 최단경로로만 이동
# 1. 태울 승객 고를 때 현재 위치에서 최단거리가 가장 짧은 승객,
# 그런 승객이 여럿이면 그 중 행 번호가 가장 작은 승객, 그 다음 열 번호 젤 작은 승객
# 연료는 한칸 이동할 때 1 소모
# 2. 목적지로 성공적으로 이동 시키면, 이동하며 소모한 연료의 2배 충전
from collections import deque

di = [0,0,1,-1]
dj = [1,-1,0,0]

# 택시 현 위치에서 젤 가까운 손님 위치 + 거리 리턴
def near_passenger(i,j):
    q = deque()
    q.append([i,j])
    dist = [[0 for _ in range(N)] for _ in range(N)]
    nears = []
    near_d = -1
    while q:
        pi, pj = q.popleft()
        if near_d != -1 and near_d < dist[pi][pj]:
            break
        #print(pi,pj)
        if board[pi][pj] < 0:
            nears.append([pi,pj,dist[pi][pj]])
            near_d = dist[pi][pj]

        for k in range(4):
            ni, nj = pi + di[k], pj + dj[k]
            if ni < 0 or nj < 0 or ni >= N or nj >= N:
                continue
            if board[ni][nj] == 1:
                continue
            if dist[ni][nj]:
                continue
            dist[ni][nj] = dist[pi][pj] + 1
            q.append([ni, nj])

    if len(nears) == 0:
        return -1
    else:
        #print(nears)
        nears = sorted(nears,key=lambda x: (x[0],x[1]))
        return nears[0]

# 시작 지점에서 끝 지점까지 드는 연료 량 리턴
def dist(start,end):
    q= deque()
    q.append(start)
    dist = [[0 for _ in range(N)] for _ in range(N)]
    while q:
        pi,pj = q.popleft()
        if pi == end[0] and pj == end[1]:
            return dist[pi][pj]
        for k in range(4):
            ni,nj = pi+di[k], pj+dj[k]
            if ni < 0 or nj < 0 or ni >= N or nj >= N:
                continue
            if board[ni][nj] == 1:
                continue
            if dist[ni][nj]:
                continue
            dist[ni][nj] = dist[pi][pj] + 1
            q.append([ni,nj])
    return -1


# 모든 승객을 성공적으로 데따 줄수 있는지 확인, 데따 줄 수 있으면 최종 남는 연료 양 출력

N,M,fuel = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
i,j = map(lambda x: int(x)-1,input().split())
guest = [list(map(lambda x: int(x)-1,input().split())) for _ in range(M)]
for ii in range(len(guest)):
    board[guest[ii][0]][guest[ii][1]] = -(ii+1)
done = [False for _ in range(M)]
done_cnt = 0

while done_cnt < M:
    #print('i,j,fuel,done', i,j,fuel,done)
    # 손님 중에 젤 가까운 놈 찾는다

    np_info = near_passenger(i,j)
    #print(np_info)
    if np_info == -1:
        break
    else:
        npi,npj,npdist = np_info
        #print('현위치에서 가장 가까운 애 {},{},{}'.format(npi,npj,npdist))
        min_i = -(board[npi][npj]) - 1
        board[npi][npj] = 0
        min_d = npdist

    # min_i,min_d = -1,987654321
    # for ii in range(M):
    #     if done[ii]:
    #         continue
    #     gi,gj = guest[ii][0],guest[ii][1]
    #     gd = dist([i,j],[gi,gj])
    #     #print('ii,dist',ii,dist([i,j],[gi,gj]))
    #     if gd == -1:
    #         continue
    #     if gd < min_d:
    #         min_i = ii
    #         min_d = gd
    # if min_i == -1:
    #     break
    #print(min_i,min_d, '로 갈 수 있나?')

    # min_i로 갈 수 있으면 간다
    if min_d <= fuel:
        fuel -= min_d
        i,j = guest[min_i][0],guest[min_i][1]
        #print('{}번 손님 출발지인 {},{}로 이동, 남은 연료: {}'.format(min_i,i,j,fuel))
    else:
        break
    # 이제 승객을 태워서 도착지로 보내자
    ed = dist([i,j],[guest[min_i][2],guest[min_i][3]])
    if ed == -1:
        break
    if ed <= fuel:
        fuel += ed
        i,j = guest[min_i][2],guest[min_i][3]
        done[min_i] = True
        done_cnt += 1
        #print('{}번 손님 목적지인 {},{}로 이동, 남은 연료: {}'.format(min_i, i, j, fuel))
    else:
        break

if done_cnt == M:
    print(fuel)
else:
    print(-1)
#print(guest)




