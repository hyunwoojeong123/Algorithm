import sys
sys.setrecursionlimit(100001)
DIV = 1000000007

def weight(now):
    global ans
    # print('weight({})'.format(now))
    visited[now] = True

    gob = 1
    for dist,child in adj[now]:
        if visited[child]:
            continue
        ret = (weight(child) * dist) % DIV
        ans += (ret * gob) % DIV
        ans %= DIV
        gob = (gob + ret) % DIV
    return gob





ans = 0
N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    A,B,W = map(int,input().split())
    adj[A].append([W,B])
    adj[B].append([W,A])
visited = [False for _ in range(N+1)]
weight(1)
print(ans)