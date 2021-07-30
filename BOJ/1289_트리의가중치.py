import sys
INF = sys.maxsize
sys.setrecursionlimit(1000001)

def weight(i,j):
    # print(i,j)
    if i == j:
        return 1
    if D[i].get(j,-1) != -1:
        return D[i][j]
    visited[i] = True
    D[i][j] = INF
    D[j][i] = INF
    for nxt in range(1,N+1):
        if nxt == i or edges[i].get(nxt,-1) == -1 or visited[nxt]:
            continue
        temp = edges[i][nxt] * weight(nxt,j) % 1000000007
        D[i][j] = min(D[i][j],temp)
        D[j][i] = D[i][j]
    visited[i] = False
    return D[i][j]

N = int(input())
edges = [dict() for i in range(N+1)]
D = [dict() for i in range(N+1)]
for _ in range(N-1):
    A,B,W = map(int,input().split())
    edges[A][B] = W
    edges[B][A] = W
    D[A][B] = W
    D[B][A] = W


ans = 0
for i in range(1,N+1):
    for j in range(i+1,N+1):
        visited = [False for _ in range(N+1)]
        ans += weight(i,j) % 1000000007

print(ans)