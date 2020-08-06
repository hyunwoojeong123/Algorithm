T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0 for col in range(10)] for row in range(10)]
    for n in range(N):
        r1_i,r1_j,r2_i,r2_j,color = list(map(int,input().split()))
        for i in range(r1_i,r2_i+1):
            for j in range(r1_j,r2_j+1):
                arr[i][j] += color
    ans = 0
    for i in range(0,10):
        for j in range(0,10):
            if arr[i][j] == 3:
                ans += 1
    print(f'#{tc} {ans}')