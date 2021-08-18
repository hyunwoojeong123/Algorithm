import sys
sys.setrecursionlimit(1000001)

def childs(prv,now):
    if D[now] != -1:
        return D[now]
    ret = 1
    for next in adj[now]:
        if next == prv:
            continue
        ret += childs(now,next)
    D[now] = ret
    return D[now]

N,R,Q = map(int,sys.stdin.readline().rstrip().split())
adj = [[] for _ in range(N+1)]
D = [-1 for _ in range(N+1)]
for _ in range(N-1):
    U,V = map(int,sys.stdin.readline().rstrip().split())
    adj[U].append(V)
    adj[V].append(U)

childs(0,R)
for _ in range(Q):
    U = int(sys.stdin.readline().rstrip())
    print(D[U])
# print(D)