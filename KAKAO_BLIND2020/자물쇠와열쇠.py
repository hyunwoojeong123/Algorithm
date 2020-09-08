def rotate(key):
    M = len(key)
    res = [[-1 for j in range(M)] for i in range(M)]
    for i in range(M):
        for j in range(M):
            res[j][M-i-1] = key[i][j]
    return res

def solution(key, lock):
    answer = False
    M, N = len(key), len(lock)
    board = [[2 for j in range(2*M+N-2)] for i in range(2*M+N-2)]
    for i in range(M-1,N+M-1):
        for j in range(M-1,N+M-1):
            board[i][j] = lock[i-M+1][j-M+1]
    # 홈 개수 세기
    homs = 0
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                homs += 1
    #print(board)
    for _ in range(4):
        key = rotate(key)
        #print('key 상태',key)
        #키 다 끼워보기
        for si in range(N+M-1):
            for sj in range(N+M-1):
                # 시작점에서 키 끼워넣는 중
                #print(si,sj, '시작점으로 검사')
                is_fit = True
                hom_cnt = 0
                for i in range(M):
                    for j in range(M):
                        #print('board[{}][{}] = {} 와 key[{}][{}] = {} 비교'.format(si+i,sj+j,board[si+i][sj+j],i,j,key[i][j]))
                        if board[si+i][sj+j] == 0 and key[i][j] == 1:
                            hom_cnt += 1
                        if board[si+i][sj+j] == 2:
                            continue
                        elif board[si+i][sj+j] + key[i][j] != 1:
                            is_fit = False
                            break

                if is_fit and hom_cnt == homs:
                    return True

    #for _ in range(4):

    return answer

key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]

print(solution(key,lock))