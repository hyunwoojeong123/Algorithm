def pick(i,sum):
    global ans
    if sum >= ans:
        return
    if i == N:
        if ans > sum:
            ans = sum
        return
    for k in range(N):
        if visited[k]:
            continue
        visited[k] = True
        pick(i+1,sum+board[i][k])
        visited[k] = False


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for i in range(N)]
    visited = [False for i in range(N)]
    ans = 9999999
    select = [-1 for i in range(N)]
    pick(0,0)
    print('#{} {}'.format(tc,ans))