import sys

def DFS(start, end):
    if start == end:
        return 0
    if D[start][end] != -1:
        return D[start][end]
    D[start][end] = INF
    for mid in range(start,end):
        left = DFS(start,mid)
        right = DFS(mid+1,end)
        alpha = 0
        if arr[start] != arr[mid+1]:
            alpha = 1
        temp = left+right+alpha
        D[start][end] = min(temp,D[start][end])
    return D[start][end]


sys.setrecursionlimit(1000000)
INF = sys.maxsize

N,K = map(int,input().split())
arr = input().split()
D = [[-1 for j in range(N+1)] for i in range(N+1)]
# N,K = 200,20
# arr = [str(i%20+1) for i in range(200)]

print(DFS(0,N-1))
# print(D)
