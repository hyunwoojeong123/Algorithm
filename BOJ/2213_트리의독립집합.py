import sys
sys.setrecursionlimit(100001)

def dokrib(prv,now):
    # print('dokrib({},{})'.format(prv,now),jibhab)
    if prv not in jibhab and D[now][1] > D[now][0]:
        jibhab.append(now)
    for next in adj[now]:
        if next == prv:
            continue
        dokrib(now,next)


def solve(prv, now, included):
    if D[now][included] != -1:
        return D[now][included]
    ret = 0
    if included == 0:
        for next in adj[now]:
            if next == prv:
                continue
            ret += max(solve(now,next,1), solve(now,next,0))
    else:
        ret += w[now]
        for next in adj[now]:
            if next == prv:
                continue
            ret += solve(now,next,0)
    D[now][included] = ret
    return D[now][included]


n = int(input())
w = [-1] + list(map(int,input().split()))
adj = [[] for _ in range(n+1)]
D = [[-1 for j in range(2)] for i in range(n+1)]
for _ in range(n-1):
    A,B = map(int,input().split())
    adj[A].append(B)
    adj[B].append(A)

ans = max(solve(0,1,0),solve(0,1,1))
jibhab = []
dokrib(0,1)
jibhab.sort()
jibhab = list(map(str,jibhab))
print(ans)
print(' '.join(jibhab))
# print(D)