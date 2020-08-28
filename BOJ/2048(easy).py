di = [0,0,1,-1] # 오,왼,아,위
dj = [1,-1,0,0]

ans = -1

def DFS(cnt,dir):
    if cnt > 5:
        global ans
        max_num = -1
        for i in range(N):
            for j in range(N):
                if max_num > board[i][j]
                    max_num = board[i][j]
        if max_num > ans:
            ans = max_num
        return
    # 판을 dir방향으로 움직인다.
    # 큐에다 0이 아닌애들 넣는다.
    # 앞에서부터 합쳐준다.
    # 0인 애들은 갯수를 새서 맞는 방향에 넣는다.
    # board의 해당 열을 걔로 대체한다.
    if dir == 0:
        for i in range(N):
            q = []
            cnt = 0
            for j in range(N):
                if board[i][j] != 0
                    q.append(board[i][j])
                else:
                    cnt += 1
            for _ in range(cnt):
                q.append(0)


N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
for dir in range(4):
    DFS(0,dir)
print(ans)
