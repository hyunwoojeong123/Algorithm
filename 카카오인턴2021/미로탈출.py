# 11:35~12:35 3:15~3:40 1:25 못 풀음
# 다익스트라 보완하고 다시 와서 풀기
def solution(n, start, end, roads, traps):
    answer = 987654321

    edges = [[[] for j in range(n + 1)] for i in range(n + 1)]
    for road in roads:
        st, ed, t = road
        edges[st][ed].append(t)

    return answer