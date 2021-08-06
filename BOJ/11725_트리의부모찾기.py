import sys
sys.setrecursionlimit(100001)

def solve(now,pnode):
    for child in adj[now]:
        if child == pnode:
            continue
        bumo[child] = now
        solve(child,now)


N = int(input())
adj = [[] for _ in range(N+1)]
bumo = [-1 for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
solve(1,0)
for i in range(2,N+1):
    print(bumo[i])

