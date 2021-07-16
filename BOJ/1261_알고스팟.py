import sys,heapq
INF = sys.maxsize
M,N = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(input())
D = [[INF for j in range(M)] for i in range(N)]
D[0][0] = 0
pq = []
#[뿌순벽개수,i,j]
heapq.heappush(pq,[0,0,0])
di = [0,0,1,-1]
dj = [-1,1,0,0]

while pq:
    cur_dist,cur_i,cur_j = heapq.heappop(pq)
    if cur_dist > D[cur_i][cur_j]:
        continue
    for k in range(4):
        next_i,next_j = cur_i+di[k],cur_j+dj[k]
        if next_i < 0 or next_j < 0 or next_i >= N or next_j >= M:
            continue
        next_dist = int(arr[next_i][next_j])
        next_dist += cur_dist
        if next_dist < D[next_i][next_j]:
            D[next_i][next_j] = next_dist
            heapq.heappush(pq,[next_dist,next_i,next_j])
print(D[N-1][M-1])
