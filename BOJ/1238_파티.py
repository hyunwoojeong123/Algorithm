import sys,heapq

INF = sys.maxsize
input = sys.stdin.readline

def dij(x):
    # d 배열을 INF 로 전부 준다
    d = [INF]*n
    # heap에다가 [0, 출발점] 을 넣는다.
    heapq.heappush(heap, [0,x])
    # d[출발점] = 0
    d[x] = 0
    # heap 다 빌 때까지 반복
    while heap:
        # w,x 는 현 위치까지의 거리와 현 위치
        w,x = heapq.heappop(heap)
        # nw,nx 는 x에서 nx까지 거리, x와 연결된 애
        for nw,nx in a[x]:
            # nw 에 w를 더해줌 : 출발점에서 nx 까지 거리
            nw += w
            # 이게 기존에 기록해둔 값보다 작으면
            if nw < d[nx]:
                # 거리 갱신하고 heap에다가 걔네 넣음.
                d[nx] = nw
                heapq.heappush(heap,[nw,nx])
    return d

n,m,t = map(int, input().split())
a = [[]*n for _ in range(n)]
heap = []

for i in range(m):
    x,y,w = map(int, input().split())
    a[x-1].append([w,y-1])

ans = [0]*n
for i in range(n):
    d = dij(i)
    ans[i] += d[t-1]
    d = dij(t-1)
    ans[i] -= d[i]
print(max(ans))