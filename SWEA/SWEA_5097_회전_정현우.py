T = int(input())
for tc in range(1,T+1):
    N,M = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    for _ in range(M):
        nums.append(nums.pop(0))
    print('#{} {}'.format(tc,nums[0]))
