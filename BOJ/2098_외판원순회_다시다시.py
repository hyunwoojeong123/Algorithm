INF = 987654321
def DFS(visit,now):
    visit = visit | (1 << now)
    if visit == (1 << N) -1:
        if edges[now][0] != 0:
            return edges[now][0]
        return INF
    if D[visit][now] != -1:
        return D[visit][now]
    D[visit][now] = INF
    for nxt in range(N):
        if edges[now][nxt] and not visit & (1 << nxt):
            dist = DFS(visit,nxt) + edges[now][nxt]
            if dist < D[visit][now]:
                D[visit][now] = dist
    return D[visit][now]


N = int(input())
edges = []
for _ in range(N):
    edges.append(list(map(int,input().split())))

D = [[-1 for j in range(N)] for i in range(1 << N)]
ans = DFS(0,0)
if ans == INF:
    print(-1)
else:
    print(ans)