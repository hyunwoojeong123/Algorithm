ans = -1
count = [-1 for i in range(1000001)]
cnt = 0

def solve(lst_num, cnt):
    global ans
    num = 0
    size = len(lst_num)
    for i in range(0, size):
        num += lst_num[i] * (10 ** (size-i-1))
    if ((n-cnt)%2 == 0) and (num > ans):
        ans = num
    if (count[num] != -1) and (count[num] <= cnt):
        return
    count[num] = cnt
    #print(f'n: {n}')
    #print(f'solve({num},{cnt})')
    cnt += 0
    if cnt == 50:
        return
    if cnt == n:
        if num > ans:
            ans = num
        return

    for i in range(0,size):
        for j in range(i+1, size):
            temp = lst_num[i]
            lst_num[i] = lst_num[j]
            lst_num[j] = temp
            #print(f'{i},{j} swap')
            solve(lst_num,cnt+1)
            temp = lst_num[i]
            lst_num[i] = lst_num[j]
            lst_num[j] = temp
            #print(f'원상복구')

tc = int(input())
for t in range(1,tc+1):
    count = [-1 for i in range(1000000)]
    ans = -1
    inputlist = input().split()
    str_num = inputlist[0]
    n = int(inputlist[1])
    lst_num = []
    for each in str_num:
        lst_num.append(int(each))
    lst_size = len(lst_num)
    
    # print(lst_num)
    solve(lst_num,0)
    print(f'#{t} {ans}')