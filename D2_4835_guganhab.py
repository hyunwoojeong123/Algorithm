T = int(input())
for tc in range(1,T+1):
    N,M = list(map(int,input().split()))
    #print(N,M)
    nums = list(map(int,input().split()))
    #print(nums)
    max_sum = -1
    min_sum = 9999999
    for i in range(0,N-M+1):
        sum = 0
        for j in range(0,M):
            sum += nums[i+j]
        max_sum = max(sum,max_sum)
        min_sum = min(sum,min_sum)
    ans = max_sum - min_sum
    print(f'#{tc} {ans}')