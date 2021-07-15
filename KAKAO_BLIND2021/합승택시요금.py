import sys, heapq


def solution(n, s, a, b, fares):
    answer = 987654321
    INF = sys.maxsize

    edges = [[] for _ in range(n + 1)]
    for fare in fares:
        st, ed, cost = fare
        edges[st].append([ed, cost])
        edges[ed].append([st, cost])

    def dkst(point):
        D = [INF for _ in range(n + 1)]
        D[point] = 0
        pq = []
        heapq.heappush(pq, [0, point])
        while pq:
            cur_cost, cur_pos = heapq.heappop(pq)
            if cur_cost > D[cur_pos]:
                continue
            for next_pos, next_cost in edges[cur_pos]:
                next_cost += cur_cost
                if next_cost < D[next_pos]:
                    D[next_pos] = next_cost
                    heapq.heappush(pq, [next_cost, next_pos])
        return D[s] + D[a] + D[b]

    for p in range(1, n + 1):
        answer = min(answer, dkst(p))

    return answer