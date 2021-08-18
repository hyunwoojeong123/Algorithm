import sys

sys.setrecursionlimit(10000)

di = [0, 0, 1, -1]  #
dj = [1, -1, 0, 0]


def solution(board):
    answer = 987654321
    N = len(board)
    D = [[[-1 for k in range(5)] for j in range(N)] for i in range(N)]

    # br 은 전 지점에서 현지점까지 도로모양 0123 에 맞는 방향 4이면 도로없음
    def DFS(i, j, cost, br):
        # print(i,j,cost,br)
        nonlocal answer
        if i == N - 1 and j == N - 1:
            answer = min(answer, cost)
            return
        if D[i][j][br] != -1 and D[i][j][br] <= cost:
            return
        D[i][j][br] = cost
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if ni < 0 or nj < 0 or ni >= N or nj >= N or board[ni][nj] == 1:
                continue
            if br == 4 or br == k:
                DFS(ni, nj, cost + 100, k)
            elif br != k:
                DFS(ni, nj, cost + 600, k)

    DFS(0, 0, 0, 4)
    return answer