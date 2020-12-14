from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 최단 경로의 값을 구하는 함수
def BFS(r, c):
    global ans
    # 위치정보와 남은 벽 제거 횟수, 이동 횟수
    q = deque()
    q.append((r, c, 1, 0))
    while True:
        if len(q) == 0: break
        curr_r, curr_c, curr_rest, curr_move = q.popleft()
        # # 이전에 방문안했으면 이동횟수 넣어줘도 되는데
        # if visited[curr_r][curr_c] == 0:
        #     visited[curr_r][curr_c] = curr_move
        # # 이전에 방문했으면 값 비교하고 더 크거나 같으면 위치정보 넣어주지 말기
        # else:
        #     if curr_move >= visited[curr_r][curr_c]:
        #         continue
        #     else:
        #         visited[curr_r][curr_c] = curr_move
        if ans != 0 and curr_move > ans:
            continue
        if curr_r == N-1 and curr_c == M-1:
            if ans == 0 or curr_move < ans:
                ans = curr_move
            continue
        # 4방향 탐색
        for a in range(4):
            nr = curr_r + dr[a]
            nc = curr_c + dc[a]
            # 범위 벗어나면 넘어가기
            if nr<0 or nr>=N or nc<0 or nc>=M:
                continue
            # 벽일 경우, 깨는 경우의 수를 q에 넣어주고 다음 방향을 탐색한다.
            if maze[nr][nc] == 1:
                # 벽 제거 횟수가 남아있어야 벽을 부술 수 있다.
                if curr_rest > 0:
                    nrest = 0
                    # 벽을 부쉈으니 벽 제거 횟수를 1 줄이고 이동횟수에 1을 더해준다.
                    # 이전에 방문하지 않았을 경우
                    if visited[nr][nc][nrest] == 0:
                        visited[nr][nc][nrest] = curr_move + 1
                        q.append((nr, nc, curr_rest - 1, curr_move + 1))
                    # 이전에 방문했을 경우 => 값 비교해서 append 할지 말지!
                    else:
                        if curr_move + 1 >= visited[nr][nc][nrest]:
                            continue
                        else:
                            visited[nr][nc][nrest] = curr_move + 1
                            q.append((nr, nc, curr_rest - 1, curr_move + 1))
                # 벽이어도 벽 제거 횟수가 0이면 벽을 부수지 않고 넘어간다.
                else:
                    continue
            # 벽이 아닐 경우
            elif maze[nr][nc] == 0:
                if visited[nr][nc][curr_rest] == 0:
                    visited[nr][nc][curr_rest] = curr_move + 1
                    q.append((nr, nc, curr_rest, curr_move + 1))
                else:
                    if curr_move + 1 >= visited[nr][nc][curr_rest]:
                        continue
                    else:
                        visited[nr][nc][curr_rest] = curr_move + 1
                        q.append((nr, nc, curr_rest, curr_move + 1))


N, M = map(int, input().split())
# 입력값 사이에 띄어쓰기 없으니까 조심
maze = [list(map(int, input())) for _ in range(N)]
# 방문 체크
visited = [[[0 for k in range(2)] for j in range(M)] for i in range(N)]
# 정답 변수
ans = 0
BFS(0, 0)
if ans == 0 and N*M != 1:
    print(-1)
else:
    print(ans + 1)