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

    # 길 정보는 정방향,역방향 나눠서 저장
    forward = [dict() for _ in range(n + 1)]
    reverse = [dict() for _ in range(n + 1)]

    for road in roads:
        st, ed, d = road
        if ed in forward[st]:
            forward[st][ed] = min(d, forward[st][ed])
        else:
            forward[st][ed] = d

        if st in reverse[ed]:
            reverse[ed][st] = min(d, reverse[ed][st])
        else:
            reverse[ed][st] = d

    D = [[INF for _ in range(n + 1)] for __ in range(1 << len(traps))]
    D[0][start] = 0
    pq = []
    heapq.heappush(pq, [0, start, 0])

    while pq:
        cur_dist, cur_node, cur_state = heapq.heappop(pq)
        if cur_node in traps:
            tidx = trap_idx[cur_node]
            # 트랩이면 상태 변경
            if cur_node in traps:
                cur_state = cur_state ^ (1 << tidx)
        # print('거리:', cur_dist,'노드:',cur_node,'상태:',cur_state)
        if cur_dist > D[cur_state][cur_node]:
            continue
        if cur_node in traps and cur_state & (1 << tidx):
            # 트랩이 활성화 대잇으면 역방향
            for next_node, next_dist in reverse[cur_node].items():
                next_dist += cur_dist
                if next_dist < D[cur_state][next_node]:
                    D[cur_state][next_node] = next_dist
                    heapq.heappush(pq, [next_dist, next_node, cur_state])
        else:
            # 정방향
            for next_node, next_dist in forward[cur_node].items():
                next_dist += cur_dist
                if next_dist < D[cur_state][next_node]:
                    D[cur_state][next_node] = next_dist
                    heapq.heappush(pq, [next_dist, next_node, cur_state])
        # if cur_node in traps:
        #     # 현 노드가 트랩이면
        #     # state 변경해주고 해당 state에 맞는 방향으로 길 찾는다.
        #     tidx = trap_idx[cur_node]
        #     next_state = cur_state ^ (1 << tidx)
        #     if next_state & (1 << tidx):
        #         # 현재 트랩 활성화댐 reverse
        #         for next_node,next_dist in reverse[cur_node].items():
        #             next_dist += cur_dist
        #             if next_dist < D[next_state][next_node]:
        #                 D[next_state][next_node] = next_dist
        #                 heapq.heappush(pq,[next_dist,next_node,next_state])
        #     else:
        #         # forward
        #         for next_node,next_dist in forward[cur_node].items():
        #             next_dist += cur_dist
        #             if next_dist < D[next_state][next_node]:
        #                 D[next_state][next_node] = next_dist
        #                 heapq.heappush(pq,[next_dist,next_node,next_state])
        # else:
        #     # 현 노드가 트랩이 아니면
        #     # 그냥 정방향으로 다음 갈애 찾는다. state변경도 없다.
        #     next_state = cur_state
        #     for next_node,next_dist in forward[cur_node].items():
        #         next_dist += cur_dist
        #         if next_dist < D[next_state][next_node]:
        #             D[next_state][next_node] = next_dist
        #             heapq.heappush(pq,[next_dist,next_node,next_state])

    # 다익스트라로 하는데
    # trap의 상태들도 같이 저장해서
    # D[trap상태][노드] 이러헤 저장할거
    # 힙큐에도 [거리,노드,trap상태] 이렇게 넣고
    # trap상태는 비트마스킹으로 표시 i번째 비트가 0이면 비활성, 1이면 활성

    for i in range(1 << len(traps)):
        if answer > D[i][end]:
            answer = D[i][end]
    return answer

print(solution(4,1,4,[[1,2,1],[3,2,1],[2,4,1]],[2,3]))