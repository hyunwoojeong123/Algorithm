import sys
input = sys.stdin.readline

def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x,y):
    p[find_set(x)] = find_set(y)

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())

    edges = [list(map(int, input().split())) for _ in range(E)]
    edges = sorted(edges, key = lambda x : x[2])

    p = [-1] * (V+1)

    for i in range(V+1):
        make_set(i)

    ans = 0
    cnt = 0
    idx = 0
    while cnt < V:
        if find_set(edges[idx][0]) != find_set(edges[idx][1]):
            union(edges[idx][0], edges[idx][1])
            cnt += 1
            ans += edges[idx][2]
        idx += 1

    print('#{} {}'.format(tc, ans))
