def DFS(p1_i,p1_j,p2_i,p2_j,idx):
    # print('DFS', p1, p2, idx)
    # print(D)
    if idx == W:
        return 0

    if D[p1_i][p1_j][p2_i][p2_j][idx] != -1:
        return D[p1_i][p1_j][p2_i][p2_j][idx]
    #1 골랏을때 거리
    dist_1 = DFS(cases[idx][0],cases[idx][1],p2_i,p2_j,idx+1) + abs(p1_i-cases[idx][0]) + abs(p1_j-cases[idx][1])
    #2 골랏을때 거리
    dist_2 = DFS(p1_i,p1_j,cases[idx][0],cases[idx][1],idx+1) + abs(p2_i-cases[idx][0]) + abs(p2_j-cases[idx][1])

    if dist_1 < dist_2:
        D[p1_i][p1_j][p2_i][p2_j][idx] = dist_1
        tk[idx] = 1
    else:
        D[p1_i][p1_j][p2_i][p2_j][idx] = dist_2
        tk[idx] = 2
    return D[p1_i][p1_j][p2_i][p2_j][idx]

INF = 987654321
N = int(input())
W = int(input())
cases = []
for _ in range(W):
    i,j = map(int,input().split())
    cases.append([i,j])

D = [[[[[-1 for _ in range(W)] for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
tk = [-1 for _ in range(W)]
print(DFS(1,1,N,N,0))
for i in range(W):
    print(tk[i])
# print(D)