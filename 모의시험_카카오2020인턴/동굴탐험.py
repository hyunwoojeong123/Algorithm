import sys

sys.setrecursionlimit(20000000)

from collections import deque


def solution(n, path, order):
    answer = True
    cnt = 0
    bi = [[] for _ in range(n)]
    uni = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    fin = [False for _ in range(n)]

    for A, B in path:
        bi[A].append(B)
        bi[B].append(A)

    q = deque()
    q.append(0)
    visited[0] = True

    while q:
        now = q.popleft()
        for next in bi[now]:
            if visited[next]:
                continue
            visited[next] = True
            uni[now].append(next)
            q.append(next)

    for A, B in order:
        uni[A].append(B)

    visited = [False for _ in range(n)]

    def dfs(node):
        nonlocal answer
        if answer == False:
            return
        visited[node] = True

        for next in uni[node]:
            if not visited[next]:
                dfs(next)
            elif not fin[next]:
                answer = False
                return

        fin[node] = True
        return

    dfs(0)
    return answer