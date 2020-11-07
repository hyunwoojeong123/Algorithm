#
#
# def DFS(i,val):
#     global MIN,MAX
#     if i == N-1:
#         if val > MAX:
#             MAX = val
#         if val < MIN:
#             MIN = val
#         return
#     for x in range(4):
#         if opers_cnt[x] > 0:
#             opers_cnt[x] -= 1
#             if x == 0:
#                 DFS(i+1, val +nums[i+1])
#             elif x == 1:
#                 DFS(i+1, val - nums[i+1])
#             elif x == 2:
#                 DFS(i+1, val * nums[i+1])
#             else:
#                 if val >= 0:
#                     DFS(i+1, val // nums[i+1])
#                 else:
#                     DFS(i+1,int(val/ nums[i+1]))
#             opers_cnt[x] += 1
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     opers_cnt = list(map(int,input().split())) # + - * // 순서
#     nums = list(map(int,input().split()))
#     MIN,MAX = 9987654321, -9987654321
#     DFS(0,nums[0])
#     #print(MIN,MAX)
#     #print(2//3)
#     print('#{} {}'.format(tc,MAX-MIN))
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    temp_board = [input() for x in range(N)]
    board = []
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(int(temp_board[i][j]))
        board.append(temp)
    visited = [[-1 for j in range(N)] for i in range(N)]
    visited[0][0] = 0
    q = [[0, 0]]
    while q:
        i, j = q.pop(0)
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if ni < 0 or nj < 0 or ni >= N or nj >= N:
                continue
            if visited[ni][nj] != -1 and visited[i][j] + board[ni][nj] >= visited[ni][nj]:
                continue
            visited[ni][nj] = visited[i][j] + board[ni][nj]
            q.append([ni, nj])
    print(f'#{tc} {visited[N - 1][N - 1]}')