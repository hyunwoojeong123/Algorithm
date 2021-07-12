# 1
# 6 5
# 0 1 0 0 0 0
# 1 0 0 0 0 0
# 0 1 0 1 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1

T = int(input())
for tc in range(1,T+1):
    W,H = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(H)]
    # print(arr)

    homes = []
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                homes.append([i,j])
    # print(homes)
    ans = 987654321
    # 가로
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                break
        else:
            max_dist = -1
            for home in homes:
                dist = abs(i-home[0])
                if max_dist < dist:
                    max_dist=dist
            # print(max_dist)
            if ans > max_dist:
                ans = max_dist

    # 세로
    for j in range(W):
        for i in range(H):
            if arr[i][j]:
                break
        else:
            # print(j)
            max_dist = -1
            for home in homes:
                dist = abs(j-home[1])
                if max_dist < dist:
                    max_dist=dist
            # print(max_dist)
            if ans > max_dist:
                ans = max_dist

    # 오른쪽 밑에가는 대각선
    # 맨 위에서 시작하는 애들
    for j in range(W):
        pi,pj = 0,j
        cnt = 0
        can = True
        jiksuns = []
        while True:
            if pi < 0 or pi >= H or pj < 0 or pj >= W:
                break
            elif arr[pi][pj]:
                can = False
                break
            else:
                jiksuns.append([pi,pj])
                cnt += 1
                pi += 1
                pj += 1
        if can and cnt >= 2:
            # print(jiksuns)
    #       이 직선으로 가장 멀리 떨어진 집과 거리를 구한다.
            max_dist = -1
            for home in homes:
                dist = 987654321
                for jiksun in jiksuns:
                    temp_dist = abs(home[0]-jiksun[0])+abs(home[1]-jiksun[1])
                    if temp_dist<dist:
                        dist = temp_dist
                if dist > max_dist:
                    max_dist=dist
            if max_dist < ans:
                ans = max_dist


    # 맨 왼쪽에서 시작하는애들
    for i in range(H):
        pi,pj = i,0
        cnt = 0
        can = True
        jiksuns = []
        while True:
            if pi < 0 or pi >= H or pj < 0 or pj >= W:
                break
            elif arr[pi][pj]:
                can = False
                break
            else:
                jiksuns.append([pi,pj])
                cnt += 1
                pi += 1
                pj += 1
        if can and cnt >= 2:
            max_dist = -1
            for home in homes:
                dist = 987654321
                for jiksun in jiksuns:
                    temp_dist = abs(home[0] - jiksun[0]) + abs(home[1] - jiksun[1])
                    if temp_dist < dist:
                        dist = temp_dist
                if dist > max_dist:
                    max_dist = dist
            if max_dist < ans:
                ans = max_dist
    # 오른쪽 위로 가는 대각선
    # 맨 왼쪽서 시작하는 애들
    for i in range(H):
        pi,pj = i,0
        cnt = 0
        can = True
        jiksuns = []
        while True:
            if pi < 0 or pi >= H or pj < 0 or pj >= W:
                break
            elif arr[pi][pj]:
                can = False
                break
            else:
                jiksuns.append([pi,pj])
                cnt += 1
                pi -= 1
                pj += 1
        if can and cnt >= 2:
            max_dist = -1
            for home in homes:
                dist = 987654321
                for jiksun in jiksuns:
                    temp_dist = abs(home[0] - jiksun[0]) + abs(home[1] - jiksun[1])
                    if temp_dist < dist:
                        dist = temp_dist
                if dist > max_dist:
                    max_dist = dist
            if max_dist < ans:
                ans = max_dist
    # 맨 아래쪽서 시작하는 애들
    for j in range(W):
        pi,pj = H-1,j
        cnt = 0
        can = True
        jiksuns = []
        while True:
            if pi < 0 or pi >= H or pj < 0 or pj >= W:
                break
            elif arr[pi][pj]:
                can = False
                break
            else:
                jiksuns.append([pi,pj])
                cnt += 1
                pi -= 1
                pj += 1
        if can and cnt >= 2:
            # print(jiksuns)
    #       이 직선으로 가장 멀리 떨어진 집과 거리를 구한다.
            max_dist = -1
            for home in homes:
                dist = 987654321
                for jiksun in jiksuns:
                    temp_dist = abs(home[0]-jiksun[0])+abs(home[1]-jiksun[1])
                    if temp_dist<dist:
                        dist = temp_dist
                if dist > max_dist:
                    max_dist=dist
            if max_dist < ans:
                ans = max_dist
    # 답 출력
    if ans == 987654321:
        ans = -1
    print('#{} {}'.format(tc,ans))