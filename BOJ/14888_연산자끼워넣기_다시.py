def DFS(idx, val):
    global MIN,MAX
    if idx == N-1:
        if val > MAX:
            MAX = val
        if val < MIN:
            MIN = val
        return
    for k in range(4):
        if oper_cnts[k] > 0:
            oper_cnts[k] -= 1
            if k == 0:
                DFS(idx+1,val+nums[idx+1])
            if k == 1:
                DFS(idx+1,val-nums[idx+1])
            if k == 2:
                DFS(idx+1,val*nums[idx+1])
            if k == 3:
                if (val < 0 and nums[idx+1] >= 0) or (val >= 0 and nums[idx+1] < 0):
                    DFS(idx+1,-(abs(val)//abs(nums[idx+1])))
                else:
                    DFS(idx+1,abs(val)//abs(nums[idx+1]))
            oper_cnts[k] += 1



N = int(input())
nums = list(map(int,input().split()))
oper_cnts = list(map(int,input().split()))
MIN = 9987654321
MAX = -99887654321
DFS(0,nums[0])
print(MAX)
print(MIN)