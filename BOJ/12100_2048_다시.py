# 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값
# 이돋할 떄 어케 이동
# 먼저 해당 줄을 다 스택에 담음
# 똑같은 애들 합침
# 어케 합치냐면 먼저 1개 꺼내고 그담꺼 끄내서 같으면 2배 해서 배열에 넣고,
# 아니면 걍 먼저 꺼낸놈 배열에 넣음
# 스택에서 꺼내서 이동하는 쪽 끝부터 넣음

di = [0,0,1,-1] # 우좌하상
dj = [1,-1,0,0]



def tilt(dir):
    if dir < 2:
        # 우 좌
        for i in range(0,N):
            st = []
            if dir == 0:
                rg = range(0,N)[::-1]
                s = N-1
            else:
                rg = range(0,N)
                s = 0
            for j in rg:
                if arr[i][j]:
                    st.append(arr[i][j])
                    arr[i][j] = 0
            # print(st)
            before = -1
            while st:
                tp = st.pop(0)
                if before == -1:
                    before = tp
                    continue
                elif before == tp:
                    arr[i][s] = before*2
                    s -= dj[dir]
                    before = -1
                else:
                    arr[i][s] = before
                    s -= dj[dir]
                    before = tp
            if before != -1:
                arr[i][s] = before
    else:
        # 하 상
        for j in range(0, N):
            st = []
            if dir == 2:
                rg = range(0, N)[::-1]
                s = N - 1
            else:
                rg = range(0, N)
                s = 0
            for i in rg:
                if arr[i][j]:
                    st.append(arr[i][j])
                    arr[i][j] = 0
            # print(st)
            before = -1
            # print(s)
            while st:
                tp = st.pop(0)
                if before == -1:
                    before = tp
                    continue
                elif before == tp:
                    arr[s][j] = before * 2
                    s -= di[dir]
                    before = -1
                else:
                    arr[s][j] = before
                    s -= di[dir]
                    before = tp
            if before != -1:
                arr[s][j] = before

def DFS(cnt):
    global ans
    if cnt == 5:
        MAX = -1
        for i in range(N):
            for j in range(N):
                if arr[i][j] > MAX:
                    MAX = arr[i][j]
        if MAX > ans:
            ans = MAX
        return
    ori_arr = [[-1 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            ori_arr[i][j] = arr[i][j]
    for k in range(4):
        tilt(k)
        DFS(cnt+1)
        for i in range(N):
            for j in range(N):
                arr[i][j] = ori_arr[i][j]

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
# print(arr)
ans = -1
DFS(0)
# print(arr)
print(ans)