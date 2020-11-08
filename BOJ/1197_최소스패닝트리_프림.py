import sys,heapq
input = sys.stdin.readline

# 1. 방문 배열 선언
# 2. heapq에 시작점 암거나 정해서 넣음
# 3. while문으로 heap빌때까지 뺀다음 걔랑 연결댄애 방문안했으면 heapq에 다 넣음

V,E = map(int,input().split())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    A,B,C = map(int,input().split())
    adj[A].append([C,B])
    adj[B].append([C,A])

visited = [False for _ in range(V+1)]

heap = []
heapq.heappush(heap,[0,1])
ans = 0
while heap:
    w,v = heapq.heappop(heap)
    if not visited[v]:
        ans += w
        visited[v] = True
        for nw,nv in adj[v]:
            if not visited[nv]:
                heapq.heappush(heap,[nw,nv])
print(ans)
