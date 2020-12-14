def DFS(i,money):
    # print('DFS({},{})'.format(i,money))
    global ans
    if i == 12:
        if money < ans:
            ans = money
        return
    if selected[i]:
        DFS(i+1,money)
    else:
        # 만약 3달 치 더했을 때, 3달이용권 쓰는게 더 싸면 select하고, 안하고 둘다 넘긴다.
        if i < 10 and moneys[i] + moneys[i+1] + moneys[i+2] > m3:
            selected[i] = True
            selected[i+1] = True
            selected[i+2] = True
            DFS(i+1,money+m3)
            selected[i] = False
            selected[i + 1] = False
            selected[i + 2] = False
        # 아니면 select안하고 money에 그 달 치만 더하고 넘김
        DFS(i+1,money+moneys[i])

T = int(input())
for tc in range(1,T+1):
    day,m1,m3,year = map(int,input().split())
    arr = list(map(int,input().split()))
    ans = 987654321
    moneys = []
    # 먼저 일일 이용권만 사용했을 때를 본다.
    for i in range(12):
        each = arr[i]*day
        # 얘랑 한달 이용꿘이랑 비교해서 짝은애를 둔다.
        if each > m1:
            each = m1
        # 얘를 저장한다.
        moneys.append(each)
    # 이제 3달 이용권을 언제 쓸지 보자. 얘는 DFS로 해서 3달 묶은게 1달 다 더한거보다 쌀 때만 한다.
    selected = [False for _ in range(12)]
    # print(moneys,selected)
    DFS(0,0)
    # 1년 이용권
    if ans > year:
        ans = year
    print('#{} {}'.format(tc, ans))