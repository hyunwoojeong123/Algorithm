def DFS(before_line,now):
    # print(before_line,now)
    if now == N:
        return 0
    if D[before_line][now] != -1:
        return D[before_line][now]
    for cur_line in range(1 << M):
        # print(bin(before_line),bin(cur_line))
        cnt_1 = 0
        pos = True
        # print('검증 간다')
        # 검증 앉기가 가능한지
        for j in range(M):
            # print(j,'번째 애 체크')
            if cur_line & (1 << j):
                cnt_1 += 1
            else:
                continue
            # 부서진 의자에 앉는 경우
            if arr[now][j] == 'x' and cur_line & (1 << j):
                pos = False
                break
            # 근처에 컨닝할수잇는애가 잇는 경우
            if j == 0:
                if cur_line & (1 << (j+1)) or before_line & (1 << (j+1)):
                    # print(cur_line & (1 << (j+1)), before_line & (1 << (j+1)))
                    # print('컨닝 가능')
                    pos = False
                    break
            elif j == M-1:
                if cur_line & (1 << (j - 1)) or before_line & (1 << (j - 1)):
                    # print(cur_line & (1 << (j - 1)), before_line & (1 << (j - 1)))
                    # print('컨닝 가능')
                    pos = False
                    break
            else:
                if cur_line & (1 << (j - 1)) or before_line & (1 << (j - 1)) or cur_line & ( 1 << (j + 1)) or before_line & (1 << (j + 1)):
                    # print(cur_line & (1 << (j - 1)), before_line & (1 << (j - 1)),cur_line & (1 << (j+1)), before_line & (1 << (j+1)) )
                    # print('컨닝 가능')
                    pos = False
                    break
        # 가능하면 temp에 DFS한 값 + 1개수 더해준다
        if pos:
            temp = cnt_1 + DFS(cur_line,now+1)
            if temp > D[before_line][now]:
                D[before_line][now] = temp
    return D[before_line][now]

C = int(input())
for t in range(C):
    N,M = map(int,input().split())
    arr = [input() for _ in range(N)]
    D = [[-1 for _ in range(N)] for _ in range(1 << M)]
    print(DFS(0,0))