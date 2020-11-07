def DFS(idx):
    global ans
    if idx == deli_sz:


        # 집과 select된 음식점들 사이의 거리 중 젤 짧은 거
        tot = 0
        for i in range(deli_sz):
            if select[i]:
                tot += deliveries[i][2]
        if tot == 0:
            return
        # print('고른 애들:',end = ' ')
        # for i in range(deli_sz):
        #     if select[i]:
        #        print(i, end = ' ')
        # #print()
        # print('운영비: ', tot)
        for home in homes:
            Min_d = 987654321
            for i in range(deli_sz):
                if select[i]:
                    dist = abs(home[0]-deliveries[i][0]) + abs(home[1]-deliveries[i][1])
                    if dist < Min_d:
                        Min_d = dist
            tot += Min_d
        if tot < ans:
            ans = tot

        #print('거리+운영비: ', tot)
        return


    select[idx] = True
    DFS(idx+1)
    select[idx] = False
    DFS(idx+1)

T = int(input())
for tc in range(1,T+1):
    ans = 987654321
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    deliveries = [] # [[위치,비용],]
    homes = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > 1:
                deliveries.append([i,j,board[i][j]])
            elif board[i][j] == 1:
                homes.append([i,j])
    deli_sz = len(deliveries)
    select = [False for _ in range(deli_sz)]
    # print(deliveries)
    # print(homes)
    #print('#{}'.format(tc))
    DFS(0)
    print('#{} {}'.format(tc, ans))
