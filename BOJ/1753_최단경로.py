import sys,heapq
INF = sys.maxsize
input = sys.stdin.readline

V,E = map(int,input().split())
K = int(input())
adj = [dict() for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    if v in adj[u]:
        adj[u][v] = min(adj[u][v],w)
    else:
        adj[u][v] = w

d = [INF for _ in range(V+1)]
d[K] = 0
pq = [[d[K],K]]

while pq:
    cur_w,cur_v = heapq.heappop(pq)
    if cur_w > d[cur_v]:
        continue
    for next_v,next_w in adj[cur_v].items():
        if d[next_v] > cur_w + next_w:
            d[next_v] = cur_w + next_w
            heapq.heappush(pq, [d[next_v],next_v])

for i in range(1,V+1):
    if d[i] == INF:
        print('INF')
    else:
        print(d[i])

0 1 2 3 4
[1 2 3 4 5]