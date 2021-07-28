import sys
INF = sys.maxsize

def DFS(state):
    # print(bin(state))
    if state == 2**(2*N)-1:
        return 0
    if D[state] != -1:
        return D[state]
    D[state] = INF
    # 먼저 방문할 놈들 정함
    for nxt in range(2*N):
        # 방문햇으면 컨티뉴
        if state & (1 << nxt):
            continue
        for adj in adjs[nxt]:
            # 근처놈도 방문햇으면 컨티뉴
            if state & (1 << adj):
                continue
            # 근처놈 + NXT 인원이 소대보다 크면 컨티뉴
            if enemy[adj] + enemy[nxt] > W:
                continue
            # 소대 침투시키기
            next_state = (state | (1 << adj)) | (1 << nxt)
            temp = DFS(next_state) + 1
            if temp < D[state]:
                D[state] = temp
        # 인접애들 방문안하는 경우도 고려해야대
        next_state = state | (1 << nxt)
        temp = DFS(next_state) + 1
        if temp < D[state]:
            D[state] = temp

    return D[state]



T = int(input())
for _ in range(T):
    N,W = map(int,input().split())
    enemy = list(map(int,input().split()))
    enemy += list(map(int,input().split()))
    # print(N,W,enemy)
    D = [-1 for _ in range(2**(2*N))]
    adjs = []
    # print(N,W,enemy)
    for i in range(2*N):
        if i == 0:
            adjs.append([i+1,N,N-1])
        elif i > 0 and i < N-1:
            adjs.append([i-1,i+1,i+N])
        elif i == N-1:
            adjs.append([i-1,0,i+N])
        elif i == N:
            adjs.append([i+1,i-N,2*N-1])
        elif i > N and i < 2*N-1:
            adjs.append([i-1,i+1,i-N])
        elif i == 2*N-1:
            adjs.append([i-1,N,i-N])
    print(N,W,enemy,adjs)
    print(DFS(0))