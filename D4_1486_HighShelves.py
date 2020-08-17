N,B,heights,ans,selected = -1,-1,[],9999999,[]

def comb(idx,n):
    global ans
    if n == 0:
        sum = 0
        for i in range(N):
            if selected[i]:
                sum += heights[i]
        if sum >=B:
            ans = min(ans,sum-B)    
        return
    for i in range(idx,N):
        if selected[i]:
            continue
        selected[i] = True
        comb(i,n-1)
        selected[i] = False

T = int(input())
for tc in range(1,T+1):
    ans = 9999999
    N,B = list(map(int,input().split()))
    heights = list(map(int,input().split()))
    selected = [False for i in range(N)]
    for n in range(1,N+1):
        comb(0,n)
    print(f'#{tc} {ans}')