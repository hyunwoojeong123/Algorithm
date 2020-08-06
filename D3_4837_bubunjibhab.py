T = int(input())
A = [i for i in range(1,13)]
n = len(A)
for tc in range(1,T+1):
    N,K = list(map(int,input().split()))
    ans = 0
    for i in range(1 << n):
        sum = 0
        cnt = 0
        for j in range(n+1):
            if i & (1<<j):
                sum += A[j]
                cnt += 1
        if sum == K and cnt == N:
            ans += 1
    print(f'#{tc} {ans}')