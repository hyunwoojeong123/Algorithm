import sys
sys.setrecursionlimit(100001)


def solve(prv,now,color):
    # print('solve({},{})'.format(now,color))
    if D[now][color] != -1:
        # print('D[{}][{}] != -1, = {}'.format(now, color, D[now][color]))
        return D[now][color]
    ret = color
    for next in adj[now]:
        if next == prv:
            continue
        temp = 987654321
        for next_color in range(1,17):
            if next_color == color:
                continue
            temp = min(temp,solve(now,next,next_color))
        ret += temp
    D[now][color] = ret
    # print('D[{}][{}] = {}'.format(now,color,D[now][color]))
    return D[now][color]


N = int(input())
adj = [[] for _ in range(N+1)]


for _ in range(N-1):
    A,B = map(int,input().split())
    adj[A].append(B)
    adj[B].append(A)


ans = 987654321
for color in range(1,17):
    # print('root를 {}로 칠했을 때'.format(color))
    D = [[-1 for j in range(17)] for i in range(N + 1)]
    ans = min(ans,solve(0,1,color))
    # print(D[1:])

print(ans)
# print(D)