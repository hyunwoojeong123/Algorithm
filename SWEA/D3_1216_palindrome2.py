import sys
sys.stdin = open("input.txt","r")
board = []

def is_pal(i,j,k):
    st_i = i
    end_i = i + k - 1
    found = True
    if end_i < 100:
        while True:
            if board[st_i][j] != board[end_i][j]:
                found = False
                break
            st_i += 1
            end_i -= 1
            if st_i >= end_i:
                break
        if found:
            return found
    st_j = j
    end_j = j + k - 1
    found = True
    if end_j < 100:
        while True:
            #print(i,st_j,i,end_j)
            if board[i][st_j] != board[i][end_j]:
                found = False;
                break;
            st_j += 1
            end_j -= 1
            if st_j >= end_j:
                break
        if found:
            return found;
    return False


def max_p_len():
    for k in range(1,101)[::-1]:
        for i in range(100):
            for j in range(100):
                if is_pal(i, j, k):
                    return k;

for tc in range(1,11):
    tnum = int(input())
    board = []
    for i in range(100):
        temp = input()
        board.append(temp)
    #print(board)
    print(f'#{tc} {max_p_len()}')
