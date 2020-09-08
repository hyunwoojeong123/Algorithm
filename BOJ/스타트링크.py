ans = 9999999999

def select(idx,cnt):
    #print(idx,cnt)
    global ans
    if cnt == N//2:
        start = 0
        link = 0
        for i in range(N):
            for j in range(i,N):
                if selected[i] and selected[j]:
                    start += S[i][j] + S[j][i]
                if not selected[i] and not selected[j]:
                    link += S[i][j] + S[j][i]
        # for k in range(N):
        #     if selected[k]:
        #         print(k,end=' ')
        # print()
        diff = abs(start-link)
        # print('diff: {}'.format(diff))
        if diff < ans:
            ans = diff
        return

    for i in range(idx,N):
        if selected[i]:
            continue
        selected[i] = True
        select(i,cnt+1)
        selected[i] = False

N = int(input())
S = [list(map(int,input().split())) for i in range(N)]
selected = [False for i in range(N)]
select(0,0)
print(ans)

