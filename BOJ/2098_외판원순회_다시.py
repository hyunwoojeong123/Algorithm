# 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 여행 경로
# 가장 비용 적은 경로의 비용을 구해라


N = int(input())
W = []
answer = 987654321
for _ in range(N):
    W.append(list(map(int,input().split())))

def BFS(start):
    D = [-1 for _ in range(1<<N)]
    # [비용,현위치,방문상태]
    D[0] = 0
    q = [[0,start,0]]
    while q:
        cur_cost,cur_node,cur_visit = q.pop(0)
        print(cur_cost,cur_node,cur_visit)
        for next_node in range(N):
            if next_node == start:
                if W[cur_node][next_node]>0 and not cur_visit & (1 << next_node) and cur_visit + (1<<next_node) == (1<<N)-1:
                    next_cost = W[cur_node][next_node]
                    next_cost += cur_cost
                    next_visit = cur_visit ^ (1 << next_node)
                    if D[next_visit] == -1 or next_cost < D[next_visit]:
                        D[next_visit] = next_cost
                        q.append([next_cost, next_node, next_visit])
            elif W[cur_node][next_node]>0 and not cur_visit & (1 << next_node):
                next_cost = W[cur_node][next_node]
                next_cost += cur_cost
                next_visit = cur_visit ^ (1 << next_node)
                if D[next_visit] == -1 or next_cost < D[next_visit]:
                    D[next_visit] = next_cost
                    q.append([next_cost,next_node,next_visit])
    return D[(1<<N)-1]


for i in range(N):
    answer = min(answer, BFS(i))
print(answer)