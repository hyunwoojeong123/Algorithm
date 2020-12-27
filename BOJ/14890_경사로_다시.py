def check(i,j,board):
    global ans
    # print(i,j)
    if j == N-1:
        ans += 1
        # print('통과!')
        return
    if board[i][j+1] == board[i][j]:
        check(i,j+1,board)
    elif board[i][j+1] - board[i][j] == 1:
        # print('오른쪽이 더큼')
        # 오른쪽이 더큼
        # 자기 포함해서 왼쪽 L칸을 체크
        chk = True
        lower = board[i][j]
        for k in range(j-L+1,j+1)[::-1]:
            # print('k:',k)
            if k < 0 or k >= N:
                chk = False
                break
            if visited[k]:
                chk = False
                break
            if board[i][k] != lower:
                chk = False
                break
        if chk:
            for k in range(j - L + 1, j + 1)[::-1]:
                visited[k] = True
            check(i,j+1,board)
    elif board[i][j+1] - board[i][j] == -1:
        # print('왼쪽이 더큼')
        # 왼쪽이 더큼
        # 자기 다음칸 포함해서 오른쪽 L칸 체크
        chk = True
        lower = board[i][j+1]
        for k in range(j+1, j+1+L):
            if k < 0 or k >= N:
                chk = False
                break
            if visited[k]:
                chk = False
                break
            if board[i][k] != lower:
                chk = False
                break
        if chk:
            for k in range(j + 1, j + 1 + L):
                visited[k] = True
            if j+L+1 == N:
                ans += 1
                # print('통과!')

                return
            else:
                check(i,j+L,board)
        pass


N,L = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
reversed = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        reversed[i].append(arr[j][i])
# print(reversed)
ans = 0

for k in range(N):
    # print('arr')
    visited = [False for _ in range(N)]
    check(k,0,arr)
    # print('reversed')
    visited = [False for _ in range(N)]
    check(k,0,reversed)
print(ans)
