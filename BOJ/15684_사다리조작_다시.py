# i번 세로선의 결과값이 i번이 나오도록 추가해야하는 가로선 개수의 최솟값?

def DFS(idx,cnt): # idx: 칸 위치 cnt : 추가한 가로선 개수 before: 이전 칸에서 설치 했는지.
    # print('DFS({},{},{})'.format(idx,cnt,adds))
    global ans
    if cnt > 3 or cnt >= ans:
        return

    # 해당 사다리 위치 체크를 안했다면 체크 하자
    # 사다리가 각번호 출발이 각번호 도착 되는지 확인
    # 되면 ans ,cnt 비교해서 작은놈으로 ans 갱신

    chk = True
    for j in range(N-1):
        start = j
        for i in range(H):
            if start != N-1 and arr[i][start]:
                start += 1
            elif start-1 >= 0 and arr[i][start-1]:
                start -= 1
        if start != j:
            chk = False
            break
    if chk:
        if ans > cnt:
            # print(cnt,'ㅎㅎ 갱신~~~~~~~~~~~~~~~~~')
            ans = cnt

    for i in range(idx, H):
        for j in range(N-1):
            if arr[i][j]:
                continue
            elif j >= 1 and arr[i][j-1]:
                continue
            elif j < N-2 and arr[i][j+1]:
                continue
            arr[i][j]= True
            DFS(i,cnt+1)
            arr[i][j] = False

N,M,H = map(int,input().split())
arr = [[False for j in range(N-1)] for i in range(H)]
checked = dict()
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    arr[a][b] = True
ans = 987654321
DFS(0,0)
if ans == 987654321:
    ans = -1
print(ans)

