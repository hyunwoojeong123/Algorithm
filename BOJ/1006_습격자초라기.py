import sys
INF = sys.maxsize

def solve(start):
    for i in range(start,N+1):
        D_both[i] = min(D_inner[i-1]+1,D_outer[i-1]+1 )
        if inner[i-1] + outer[i-1] <= W:
            D_both[i] = min(D_both[i], D_both[i-1]+1)
        if i > 1 and inner[i-1]+inner[i-2] <= W and outer[i-1]+outer[i-2] <= W:
            D_both[i] = min(D_both[i], D_both[i-2]+2)
        if i == N:
            continue
        D_inner[i] = INF
        D_inner[i] = min(D_inner[i-1]+2,D_inner[i])
        if inner[i] + inner[i-1] <= W:
            D_inner[i] = min(D_outer[i-1]+1,D_inner[i])
        D_inner[i] = min(D_inner[i],D_both[i]+1)

        D_outer[i] = INF
        D_outer[i] = min(D_outer[i - 1] + 2, D_outer[i])
        if outer[i] + outer[i - 1] <= W:
            D_outer[i] = min(D_inner[i - 1] + 1, D_outer[i])
        D_outer[i] = min(D_outer[i], D_both[i] + 1)

T = int(input())
for _ in range(T):
    ans = 987654321
    N,W = map(int,input().split())
    inner = list(map(int,input().split()))
    outer = list(map(int,input().split()))

    D_inner = [-1 for _ in range(N)]
    D_outer = [-1 for _ in range(N)]
    D_both = [-1 for _ in range(N+1)]

    # 둘다 연결안하는 경우
    D_inner[0] = 1
    D_outer[0] = 1
    D_both[0] = 0
    solve(1)

    ans = min(ans,D_both[N])
    # print('둘다연결안함',D_inner, D_outer, D_both,ans)
    # inner 만 연결
    if N > 1 and inner[0] + inner[N-1] <= W:
        D_inner[1] = 2
        if outer[0] + outer[1] <= W:
            D_outer[1] = 1
        else:
            D_outer[1] = 2
        D_both[1] = 1
        solve(2)
        ans = min(ans,D_outer[N-1]+1)
        # print('inner만 연결', D_inner, D_outer, D_both, ans)
    # outer만 연결
    if N > 1 and outer[0] + outer[N-1] <= W:
        D_outer[1] = 2
        if inner[0] + inner[1] <= W:
            D_inner[1] = 1
        else:
            D_inner[1] = 2
        D_both[1] = 1
        solve(2)
        ans = min(ans,D_inner[N-1]+1)
        # print('outer만 연결', D_inner, D_outer, D_both, ans)
    # 둘다 연결
    if N > 1 and inner[0] + inner[N-1] <= W and outer[0] + outer[N-1] <= W:
        D_outer[1] = 1
        D_both[1] = 0
        D_inner[1] = 1
        solve(2)
        ans  = min(ans,D_both[N-1]+2)
        # print('둘다 연결', D_inner, D_outer, D_both, ans)
    print(ans)