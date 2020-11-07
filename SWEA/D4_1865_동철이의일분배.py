def sunyul(cnt, pct):
    global ans
    if pct < ans:
        return
    if cnt == N:
        #print(match)
        if pct > ans:
            ans = pct
        return
    for idx in range(N):
        if selected[idx]:
            continue
        selected[idx] = True
        match[cnt] = idx
        sunyul(cnt+1, pct*arr[cnt][idx]/100)
        selected[idx] = False

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for i in range(N)]
    selected = [False for i in range(N)]
    match = [-1 for i in range(N)]
    ans = 0
    sunyul(0,1)
    ans *= 100

    print('#{}'.format(tc), '%.6f' % ans)
