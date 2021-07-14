# 2:30~2:50

import sys,heapq
INF = sys.maxsize
input = sys.stdin.readline

N = int(input())
M = int(input())
bus = [dict() for _ in range(N+1)]
for _ in range(M):
    st,ed,cost = map(int,input().split())
    if ed in bus[st]:
        bus[st][ed] = min(bus[st][ed],cost)
    else:
        bus[st][ed] = cost
    # bus[st].append([cost,ed])
start,end = map(int,input().split())

# print(N,M,bus,start,end)
D = [INF for _ in range(N+1)]
D[start] = 0
pq = []
heapq.heappush(pq,[0,start])

# print(pq,D)

while pq:
    cost,city = heapq.heappop(pq)
    # print(cost,city)
    if cost > D[city]:
        continue
    for ncity,ncost in bus[city].items():
        # print(ncost,ncity)
        ncost += cost
        if ncost < D[ncity]:
            D[ncity] = ncost
            heapq.heappush(pq,[ncost,ncity])

print(D[end])
