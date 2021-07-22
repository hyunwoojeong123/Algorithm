def DFS(node,d):
    # print(node,d)
    global ans
    visited[node] = True
    if D[node] < d:
        D[node] = d
    for nxt_node,nxt_d in edges[node]:
        if not visited[nxt_node]:
            DFS(nxt_node,d+nxt_d)

    visited[node] = False

V = int(input())
edges = [[] for _ in range(V+1)]
visited = [False for _ in range(V+1)]
# node 1에서 여까지 걸리는 거리
D = [-1 for _ in range(V+1)]
D[1] = 0
ans = -1
for _ in range(V):
    ips = list(map(int,input().split()))
    node = ips[0]
    links= ips[1:-1]
    for i in range(0,len(links),2):
        edges[node].append([links[i],links[i+1]])
DFS(1,0)
max_i = 1
for i in range(len(D)):
    if D[max_i] < D[i]:
        max_i = i
D = [-1 for _ in range(V+1)]
D[max_i] = 0
DFS(max_i,0)
print(max(D))