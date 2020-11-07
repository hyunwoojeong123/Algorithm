# edges를 가중치가 작은 게 앞에 오게 sort E*logE
# 싸이클 안생기게 유니온 파인드로 같은 부모인지 확인하면서 간다
# 다 연결댈 때까지만 한다

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x,y):
    p[find_set(x)] = find_set(y)

V,E = map(int,input().split())
edges = []
for _ in range(E):
    st,ed,w = map(int,input().split())
    edges.append([st,ed,w])
p = [x for x in range(V+1)]

edges = sorted(edges, key = lambda x : x[2])
cnt = 1
idx = 0
ans = 0

while cnt < V and idx < E:
    x,y,w = edges[idx]
    if find_set(x) != find_set(y):
        union(x,y)
        cnt += 1
        ans += w
    idx += 1
print(ans)


