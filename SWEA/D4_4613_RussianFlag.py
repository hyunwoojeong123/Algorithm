# 가운데 애들은 일단 시작은 흰색 아니면 파란색.
# 근데 가운데 중 최소 한 줄은 파란색이어야 함.
# 파란색으로 칠했으면, 그담 부터는 파랑 아니면 빨강
# 빨강으로 칠했으면, 그담 부터는 무조건 빨강
# 따라서 파란색,빨간색 칠했음을 나타내는 표시가 있어야함
# 걔네를 DFS에 인자로 줌

# 해당 줄에서 그 색이 아닌애들 세는거
def count_not_color(i,color):
    not_color = 0
    for j in range(M):
        if board[i][j] != color:
            not_color += 1
    return not_color

def DFS(i,painted_blue,painted_red,cnt):
    if i == N-1:
        #print(cnt,row_color)
        # 파란색 칠해져 있을 때만 답임
        if painted_blue:
            global ans
            if cnt < ans:
                ans = cnt
        return
    # i번째 줄을 칠한다.
    # 파랑 색 안칠했으면, 흰색,파랑색 칠 가능
    if not painted_blue:
        # 흰색 으로 칠함.
        not_white = count_not_color(i,'W')
        # 다음 줄 칠하러 감
        row_color[i] = 'W'
        DFS(i+1,False,False,cnt+not_white)
        # 파랑색으로 칠함
        row_color[i] = 'B'
        not_blue = count_not_color(i,'B')

        DFS(i+1,True,False,cnt+not_blue)
    # 파랑색 칠 했을 때
    else:
        # 빨강을 이미 칠한 경우 빨강만 칠 가능
        if painted_red:
            not_red = count_not_color(i,'R')
            row_color[i] = 'R'
            DFS(i+1,True,True,cnt+not_red)
        # 빨강을 안 칠한 경우 파랑,빨강 가능
        else:
            not_blue = count_not_color(i,'B')
            row_color[i] = 'B'
            DFS(i+1,True,False,cnt+not_blue)
            row_color[i] = 'R'
            not_red = count_not_color(i,'R')
            DFS(i+1,True,True,cnt+not_red)

T = int(input())
for tc in range(1,T+1):
    N,M = list(map(int,input().split()))
    ans = 987654321
    board = []
    for _ in range(N):
        board.append(list(input()))
    cnt = 0
    row_color = ['' for i in range(N)]
    row_color[0],row_color[N-1] = 'W','R'
    # 첫 한 줄은 무조건 흰색
    # 마지막 한 줄은 무조건 빨간색
    # 아닌 애들 cnt에 추가
    for j in range(M):
        if board[0][j] != 'W':
            cnt += 1
        if board[N-1][j] != 'R':
            cnt += 1
    # print(cnt)
    DFS(1,False,False,cnt)
    print('#{} {}'.format(tc,ans))
