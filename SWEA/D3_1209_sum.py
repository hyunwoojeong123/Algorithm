import sys
sys.stdin = open("input.txt","r")

for tc in range(1,11):
    tnum = input()
    board = []
    for i in range(0,100):
        board.append(list(map(int,input().split())))
    #print(board)
    ans = -1
    # 가로 세로 체크
    for i in range(0 ,100):
        garo_sum = 0
        sero_sum = 0
        for j in range(0,100):
            garo_sum += board[i][j]
            sero_sum += board[j][i]
        ans = max(garo_sum,sero_sum,ans)
    # 대각 체크
    daegak_sum1 = 0
    daegak_sum2 = 0
    for i in range(0,100):
        daegak_sum1 += board[i][i]
        daegak_sum2 += board[i][9-i]
    ans = max(daegak_sum1, daegak_sum2, ans)
    print(f'#{tc} {ans}')