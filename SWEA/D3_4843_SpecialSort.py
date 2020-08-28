T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    ans = []
    for i in range(0,10):
        if i % 2 == 0:
            num = max(arr)
        else:
            num = min(arr)
        ans.append(num)
        arr.remove(num)
    str_ans = ''
    for i in range(0,10):
        str_ans += ' ' + str(ans[i])
    print(f'#{tc}{str_ans}')

