N = -1
def rotate(board):
    res = []
    for j in range(N):
        temp = []
        for i in range(N):
            temp.append(board[N-i-1][j])
        res.append(temp)
    return res

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for x in range(N)]
    board_90 = rotate(board)
    board_180 = rotate(board_90)
    board_270 = rotate(board_180)
    print(f'#{tc}')
    ans = []
    for i in range(N):
        temp = ''
        for j in range(N):
            temp += str(board_90[i][j])
        temp += ' '
        for j in range(N):
            temp += str(board_180[i][j])
        temp += ' '
        for j in range(N):
            temp += str(board_270[i][j])
        ans.append(temp)
    for i in range(N):
        print(ans[i])

