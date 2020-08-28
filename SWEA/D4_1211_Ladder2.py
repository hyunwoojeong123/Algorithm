# import sys
# sys.stdin = open("input.txt","r")
#
# board,visited = [],[]
# ans = -1
# ans_len = 10000
# di = [0,0,1] # 왼 오 아
# dj = [-1,1,0]
# flag = False
#
# def find_way(i,j,dist):
#     visited[i][j] = True
#     #print(i,j,dist)
#     if i == 99:
#         #print(f'{i},{j}, {board[i][j]}, {dist}에 도착')
#         global ans, ans_len, flag
#         if dist <= ans_len:
#             ans_len = dist
#             flag = True
#             return
#     else:
#         for k in range(3):
#             ni,nj = i + di[k], j + dj[k]
#             if ni < 0 or nj < 0 or ni >= 100 or nj >= 100 or visited[ni][nj] or board[ni][nj] == 0:
#                 continue
#             else:
#                 find_way(ni,nj,dist+1)
#                 break
#
# for tc in range(1,11):
#     tnum = input()
#     board = [list(map(int,input().split())) for i in range(100)]
#     starts = []
#     ans = -1
#     ans_len = 10000
#     for j in range(100):
#         if board[0][j] == 1:
#             starts.append(j)
#     for start in starts:
#         #print('{} 탐색시작'.format(start))
#         visited = [[False for j in range(100)] for i in range(100)]
#         flag = False
#         find_way(0,start,0)
#         if flag:
#             ans = start
#     print('#{} {}'.format(tc,ans))

print(bool(-1))