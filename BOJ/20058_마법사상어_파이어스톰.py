# 회전 어케 시키냐
#
from collections import deque
def rotate(si,sj,L):
    new = [[-1 for _ in range(2**L)] for _ in range(2**L)]
    for i in range(2**L):
        for j in range(2**L):
            new[i][j] = arr[si+i][sj+j]
    #print(new)
    # new를 뒤집고
    tp = [[-1 for _ in range(2**L)] for _ in range(2**L)]
    for i in range(2**L):
        for j in range(2**L):
            tp[i][j] = new[2**L-1-j][i]
    for i in range(2**L):
        for j in range(2**L):
            new[i][j] = tp[i][j]
    # arr에 저장
    for i in range(2**L):
        for j in range(2**L):
            arr[si+i][sj+j] = new[i][j]

def BFS(i,j):
    q = deque()
    cnt = 1
    q.append([i,j])
    visited[i][j] = True
    while q:
        pi,pj = q.popleft()
        for k in range(4):
            ni,nj = pi + di[k], pj + dj[k]
            if ni < 0 or nj < 0 or ni >= 2**N or nj >= 2**N:
                continue
            if visited[ni][nj]:
                continue
            if arr[ni][nj] == 0:
                continue
            q.append([ni,nj])
            visited[ni][nj] = True
            cnt += 1
    return cnt


di = [0,0,1,-1]
dj = [1,-1,0,0]

N,Q = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(2**N)]
new = [[-1 for _ in range(2**N)] for _ in range(2**N)]
cnts = [[-1 for _ in range(2**N)] for _ in range(2**N)]
visited = [[False for _ in range(2**N)] for _ in range(2**N)]
Ls = list(map(int,input().split()))

# 1. 격자를 2**L x 2**L 로 나눈다.
# 2. 모든 부분 격자를 시계 방향으로 90도 회전시킨다.
# 3. 얼음이 있는 칸 3개 이상과 인접해 있지 않은 칸은 얼음의 양이 1 줄어든다.
# 총 Q번 반복
# 출력 : 1) 남아있는 얼음들의 총 합
# 2) 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수

#O(Q*(2**2N))
for L in Ls:
    # 1,2
    for i in range(0,2**N,2**L):
        for j in range(0, 2**N, 2**L):
            # O(2**2L)
            rotate(i,j,L)
    # for i in range(0,2**N):
    #     for j in range(0,2**N):
    #         print(arr[i][j], end = ' ')
    #     print()

    # 3

    for i in range(2**N):
        for j in range(2**N):
            if arr[i][j] == 0:
                continue
            cnt = 0
            for k in range(4):
                ni,nj = i + di[k],j + dj[k]
                if ni < 0 or nj < 0 or ni >= 2**N or nj >= 2**N:
                    continue
                if arr[ni][nj] > 0:
                    cnt += 1
            cnts[i][j] = cnt
    for i in range(2**N):
        for j in range(2**N):
            if arr[i][j] == 0:
                continue
            if cnts[i][j] < 3 and arr[i][j] > 0:
                arr[i][j] -= 1

# 출력
#얼음 총 합
hab = 0
for i in range(2**N):
    for j in range(2**N):
        hab += arr[i][j]
print(hab)

big = 0
#얼음중 가장 큰 덩어리
for i in range(2**N):
    for j in range(2**N):
        if arr[i][j] and not visited[i][j]:
            mess = BFS(i,j)
            if big < mess:
                big = mess
print(big)