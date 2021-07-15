import sys, heapq


def solution(n, start, end, roads, traps):
    answer = 987654321
    INF = sys.maxsize
    # trap_idx 는 해당 노드가 트랩이면 트랩스에서 몇번째 idx인지 리턴

    trap_idx = dict()
    for i in range(len(traps)):
        trap = traps[i]
        trap_idx[trap] = i
    # print(trap_idx)

    # 길 정보는 정방향 1,역방향 0로 저장
    edges = [[] for _ in range(n + 1)]
    for road in roads:
        st, ed, d = road
        edges[st].append([ed, d, 1])
        edges[ed].append([st, d, 0])
    # print(edges)

    D = [[INF for _ in range(n + 1)] for __ in range(1 << len(traps))]
    D[0][start] = 0
    pq = []
    heapq.heappush(pq, [0, start, 0])

    while pq:
        cur_dist, cur_node, cur_state = heapq.heappop(pq)
        cur_tidx = -1
        if cur_node in traps:
            cur_tidx = trap_idx[cur_node]
        # print('거리:', cur_dist,'노드:',cur_node,'상태:',cur_state)
        if cur_dist > D[cur_state][cur_node]:
            continue
        for next_node, next_dist, is_forward in edges[cur_node]:
            # 가려는 곳이 트랩인지 아닌지 구분해서 상태 변경 처리한다.
            next_state = cur_state
            next_tidx = -1
            if next_node in traps:
                next_tidx = trap_idx[next_node]
                next_state = next_state ^ (1 << next_tidx)
            ## 일반->일반
            if cur_node not in traps and next_node not in traps:
                if is_forward:
                    next_dist += cur_dist
                    if next_dist < D[next_state][next_node]:
                        D[next_state][next_node] = next_dist
                        heapq.heappush(pq, [next_dist, next_node, next_state])
            ## 일반->트랩
            elif cur_node not in traps and next_node in traps:
                if is_forward and not cur_state & (1 << next_tidx):
                    next_dist += cur_dist
                    if next_dist < D[next_state][next_node]:
                        D[next_state][next_node] = next_dist
                        heapq.heappush(pq, [next_dist, next_node, next_state])
                elif not is_forward and cur_state & (1 << next_tidx):
                    next_dist += cur_dist
                    if next_dist < D[next_state][next_node]:
                        D[next_state][next_node] = next_dist
                        heapq.heappush(pq, [next_dist, next_node, next_state])

            ## 트랩->트랩
            elif cur_node in traps and next_node in traps:
                if is_forward:
                    if (cur_state & (1 << cur_tidx) and cur_state & (1 << next_tidx)) or (
                            not (cur_state & (1 << cur_tidx)) and not (cur_state & (1 << next_tidx))):
                        next_dist += cur_dist
                        if next_dist < D[next_state][next_node]:
                            D[next_state][next_node] = next_dist
                            heapq.heappush(pq, [next_dist, next_node, next_state])
                else:
                    if (not (cur_state & (1 << cur_tidx)) and cur_state & (1 << next_tidx)) or (
                            (cur_state & (1 << cur_tidx)) and not (cur_state & (1 << next_tidx))):
                        next_dist += cur_dist
                        if next_dist < D[next_state][next_node]:
                            D[next_state][next_node] = next_dist
                            heapq.heappush(pq, [next_dist, next_node, next_state])
            ## 트랩->일반
            elif cur_node in traps and next_node not in traps:
                if is_forward:
                    if not (cur_state & (1 << cur_tidx)):
                        next_dist += cur_dist
                        if next_dist < D[next_state][next_node]:
                            D[next_state][next_node] = next_dist
                            heapq.heappush(pq, [next_dist, next_node, next_state])
                else:
                    if cur_state & (1 << cur_tidx):
                        next_dist += cur_dist
                        if next_dist < D[next_state][next_node]:
                            D[next_state][next_node] = next_dist
                            heapq.heappush(pq, [next_dist, next_node, next_state])

    for i in range(1 << len(traps)):
        if answer > D[i][end]:
            answer = D[i][end]
    return answer