import sys
sys.stdin = open("input.txt","r")

def check(board):
    # 가로 체크
    for i in range(0, 9):
        checked_garo = [False for x in range(0, 10)]
        for j in range(0, 9):
            num_garo = board[i][j]
            if checked_garo[num_garo]:
                #print(f'{i}행에서 걸림')
                return 0
            checked_garo[num_garo] = True
    # 세로 체크
    for i in range(0, 9):
        checked_sero = [False for x in range(0, 10)]
        for j in range(0, 9):
            num_sero = board[j][i]
            if checked_sero[num_sero]:
                #print(f'{i}열에서 걸림')
                return 0
            checked_sero[num_sero] = True
    # 네모 체크
    for m in range(0,3):
        for n in range(0,3):
            #print(f'{m},{n} 네모')
            checked_nemo = [False for x in range(0, 10)]
            for i in range(m*3,m*3+3):
                for j in range(n*3,n*3+3):
                    #print(f'{i},{j}')
                    num_nemo = board[i][j]
                    if checked_nemo[num_nemo]:
                        #print(f'{m},{n} 번째 네모에서 걸림')
                        return 0
                    checked_nemo[num_nemo] = True
    return 1

T = int(input())
for tc in range(1,T+1):
    board = []
    for i in range(9):
        board.append(list(map(int,input().split())))
    print(f'{tc} {check(board)}')
