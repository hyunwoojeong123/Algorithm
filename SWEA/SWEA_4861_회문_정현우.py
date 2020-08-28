T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    board = []
    for i in range(N):
        temp = input()
        tp = []
        for char in temp:
            tp.append(char)
        board.append(tp)
    ans = ''
    # 가로 찾기.
    for i in range(N):
        for j in range(N - M + 1):
            for k in range(M // 2):
                if board[i][j + k] != board[i][-k - 1]:
                    break
            else:
                ans = ''.join(board[i][j:j + M])
    # 세로 찾기.
    for j in range(N):
        for i in range(N - M + 1):
            for k in range(M // 2):
                if board[i + k][j] != board[-k - 1][j]:
                    break
            else:
                for l in range(M):
                    ans += board[i + l][j]

    print(f'#{tc} {ans}')