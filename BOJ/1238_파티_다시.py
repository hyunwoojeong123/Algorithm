import sys,heapq
INF = sys.maxsize

# 다익스트라
def dijk(x):
    d = [INF for _ in range(N+1)]
    d[x] = 0
    pq = [[d[x],x]]
    while pq:
        cur_w,cur_v = heapq.heappop(pq)
        #print(cur_w,cur_v)
        if cur_w > d[cur_v]:
            continue
        for next_w,next_v in adj[cur_v]:
            if d[next_v] > cur_w + next_w:
                d[next_v] = cur_w + next_w
                heapq.heappush(pq,[d[next_v],next_v])
    return d

N,M,X = map(int,input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    st,ed,w = map(int,input().split())
    adj[st].append([w,ed])


ans = [0 for _ in range(N+1)]
for i in range(1,N+1):
    d = dijk(i)
    ans[i] += d[X]
    d = dijk(X)
    ans[i] += d[i]
print(max(ans))

