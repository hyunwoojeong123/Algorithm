def DFS(num_str,cnt):
    #print(num_str,cnt)
    global ans
    num_int = int(num_str)
    if num_int > ans and cnt % 2 == 0:
        ans = num_int
    if visited[num_int]:
        return
    if cnt == 0:
        return
    visited[num_int] = True
    num_lst = list(num_str)
    for i in range(N):
        for j in range(i+1,N):
            if i == j:
                continue
            #print(num_str,'에서',i,j,'swap')
            #print(num_lst[i], num_lst[j])
            num_lst[i],num_lst[j] = num_lst[j], num_lst[i]
            DFS(''.join(num_lst),cnt-1)
            num_lst[i], num_lst[j] = num_lst[j], num_lst[i]




T = int(input())
for tc in range(1,T+1):
    num_str,cnt = input().split()
    cnt = int(cnt)
    N = len(num_str)
    visited = [False for j in range(1000000)]
    ans = 0
    DFS(num_str,cnt)
    print('#{} {}'.format(tc, ans))
