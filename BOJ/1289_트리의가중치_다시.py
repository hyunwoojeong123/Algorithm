import sys
sys.setrecursionlimit(100001)

def weight(node):
    global ans
    visited[node] = True
    gob = 1
    for child,dist in adj[node]:
        if visited[child]:
            continue
        ret = weight(child) * dist % 1000000007
        ans += ret*gob % 1000000007
        ans %= 1000000007
        gob += ret % 1000000007
    return gob

N = int(input())
adj = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(N-1):
    A,B,W = map(int,input().split())
    adj[A].append([B,W])
    adj[B].append([A,W])
ans = 0
weight(1)
print(ans)