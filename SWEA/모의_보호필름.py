from pprint import pprint
def DFS(cnt, idx):
    global ans
    if cnt >= ans:
        return
    # print('DFS({}, {})'.format(cnt,idx))
    # pprint(arr)
    # 테스트
    test = True
    for j in range(W):
        serial = 0
        before = arr[0][j]
        for i in range(D):
            # print(i,j,serial)
            if arr[i][j] == before:
                serial += 1
            else:
                before = arr[i][j]
                serial = 1
            if serial >= K:
                break
        else:
            # print('{} 행에서 실패'.format(j))
            test = False
            break
    if test:
        # print('{}에서 테스트통과~')
        if cnt < ans:
            ans = cnt
    for i in range(idx,D):
        if checked[i]:
            continue
        checked[i] = True
        # 다 A로 바꿈
        temp = []
        for j in range(W):
            temp.append(arr[i][j])
        for j in range(W):
            arr[i][j] = 0
        DFS(cnt+1,i)
        # 다 B로 바꿈
        for j in range(W):
            arr[i][j] = 1
        DFS(cnt+1,i)
        # 원상 복구
        for j in range(W):
            arr[i][j] = temp[j]
        checked[i] = False

T = int(input())
for tc in range(1,T+1):
    D,W,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(D)]
    ans = 987654321
    checked = [False for _ in range(D)]
    DFS(0,0)
    print('#{} {}'.format(tc,ans))