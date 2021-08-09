def solution(m, n, board):
    answer = 0
    my_board = []
    for each in board:
        temp = []
        for e in each:
            temp.append(e)
        my_board.append(temp)
    board = my_board

    def printBoard():
        for i in range(m):
            print(board[i])
        print()

    while True:
        # printBoard()
        will_die_cnt = 0
        will_die = [[False for j in range(n)] for i in range(m)]
        for si in range(m - 1):
            for sj in range(n - 1):
                ref = board[si][sj]
                if ref == '.':
                    continue
                if board[si][sj] == ref and board[si + 1][sj] == ref and board[si][sj + 1] == ref and board[si + 1][
                    sj + 1] == ref:
                    will_die[si][sj] = True
                    will_die[si][sj + 1] = True
                    will_die[si + 1][sj] = True
                    will_die[si + 1][sj + 1] = True
        for i in range(m):
            for j in range(n):
                if will_die[i][j]:
                    will_die_cnt += 1
                    board[i][j] = '.'

        if will_die_cnt == 0:
            break
        else:
            answer += will_die_cnt
            for j in range(n):
                q = []
                for i in range(m)[::-1]:
                    if board[i][j] != '.':
                        q.append(board[i][j])
                # print(q)
                for i in range(m):
                    board[i][j] = '.'
                pi = m - 1
                while q:
                    board[pi][j] = q.pop(0)
                    pi -= 1
            # print(will_die_cnt,'개의 블록 없앰')
            # printBoard()

    return answer