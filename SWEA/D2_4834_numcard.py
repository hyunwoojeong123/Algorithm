T = int(input())
for tc in range(1,T+1):
    N = int(input())
    str = input()
    #print(str)
    nums = []
    for char in str:
        nums.append(int(char))
    #print(nums)
    max_num = -1
    max_cnt = 0
    for i in range(0,10):
        cnt = 0
        for j in range(len(nums)):
            if i == nums[j]:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            max_num = i
        elif cnt == max_cnt:
            max_num = i

    print(f'#{tc} {max_num} {max_cnt}')