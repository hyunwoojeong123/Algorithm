def comb(idx, cnt):
    global ans
    if cnt == N//2:
        # 계산해서 ans 갱신
        sels,nosels = [],[]
        for i in range(N):
            if selected[i]:
                sels.append(i)
            else:
                nosels.append(i)
        sel = 0
        nosel = 0
        for i in range(N//2):
            A = sels[i]
            C = nosels[i]
            for j in range(i+1,N//2):
                B = sels[j]
                D = nosels[j]
                sel += arr[A][B] + arr[B][A]
                nosel += arr[C][D] + arr[D][C]
        tp = abs(sel-nosel)
        if tp < ans:
            ans = tp
        return
    for i in range(idx,N):
        if selected[i]:
            continue
        selected[i] = True
        comb(i,cnt+1)
        selected[i] = False

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 주의점 1->0 1씩 빼줘야함
    #먼저 comb로 고르자
    ans = 987654321
    selected = [False for _ in range(N)]
    comb(0,0)
    print('#{} {}'.format(tc, ans))