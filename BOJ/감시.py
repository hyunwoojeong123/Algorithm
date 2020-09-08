# DFS로 푼다.
# CCTV인 애들을 따로 리스트에 담아 둔다.
# DFS로 첨부터 끝까지 걔네들의 방향을 설정한다.
# DFS의 종료조건은 모든 캠의 방향이 정해지면,
# 사각지대의 크기를 구한다.

di = [0,1,0,-1]
dj = [1,0,-1,0]

cam_dirs = [[],
            [[0],[1],[2],[3]],
            [[2,0],[3,1]],
            [[0,3],[2,3],[1,2],[0,1]],
            [[0,2,3],[1,2,3],[0,1,2],[0,1,3]],
            [[0,1,2,3]]]

def DFS(i):
    global K
    if i == K:
        for c in choosed_dirs:
            print(c,end = ' ')
        print()
        # 배열에 감시지역 체크,
        gamsid = [[-1 for j in range(M)] for i in range(N)]
        for i in range(N):
            for j in range(M):
                gamsid[i][j] = board[i][j]

        return
    cam_i,cam_j = cams[i][0],cams[i][1]
    cam_num = board[cam_i][cam_j]
    for k in range(len(cam_dirs[cam_num])):
        choosed_dirs[i] = k
        DFS(i+1)

ans = 9999999

N,M = list(map(int,input().split()))
board = [list(map(int,input().split())) for i in range(N)]
cams = []
for i in range(N):
    for j in range(M):
        if board[i][j] >= 1 and board[i][j] <= 5:
            cams.append([i,j])
print(cams)
K = len(cams)
choosed_dirs = [-1 for _ in range(K)]
DFS(0)