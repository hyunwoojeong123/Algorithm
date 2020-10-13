# 명령 처리, board에다 건물 처리 해준 다음에
# 그 다음에 최종적으로 ans에 담는다.
N = -1
board = [[[]]]

def do(x,y,target,order):
    #print(board)
    if order == 0:
        # 삭제
        board[x][y][target] = False
    else:
        board[x][y][target] = True

def check_pos(x,y,target):
    if target == 0:
        # 기둥: 0
        # 바닥에 있으면,
        if y == 0:
            return True
        # 보의 한쪽 끝 부분 위에 있거나
        if (x > 0 and board[x-1][y][1]) or (x < N and board[x][y][1]):
            return True
        #또는 다른 기둥 위에 있을 때
        if (y > 0 and board[x][y-1][0]):
            return True
    else:
        # 보 : 1
        # 보는 한쪽 끝 부분이 기둥위에 있거나,
        if y > 0 and (board[x][y-1][0] or board[x+1][y-1][0]):
            return True
        # 양쪽 끝 부분이 다른 보와 동시에 연결
        if (x >= 1 and board[x-1][y][1]) and (x < N and board[x+1][y][1]):
            return True
    return False

# 지금 board가 규칙에 맞는지 확인
def check_board():
    for x in range(N+1):
        for y in range(N+1):
            for target in range(2):
                if board[x][y][target]:
                    if not check_pos(x,y,target):
                        return False
    return True

def solution(n, build_frame):
    global N,board
    N = n
    answer = []
    board = [[[False for k in range(2)] for j in range(n+1)] for i in range(n+1)]
    for build in build_frame:
        x,y,target,order = build[0],build[1],build[2],build[3]
        do(x,y,target,order)
        opp_order = 0
        if order == 0:
            opp_order = 1
        if not check_board():
            do(x,y,target,opp_order)
    # board에 있는 애들 answer에 담기
    for x in range(N+1):
        for y in range(N+1):
            for target in range(2):
                if board[x][y][target]:
                    answer.append([x,y,target])



    return answer

# n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],
#                [5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# print(solution(n,build_frame))
