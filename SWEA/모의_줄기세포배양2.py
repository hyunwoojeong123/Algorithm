from pprint import pprint
dx = [0, 0, -1, 1];dy = [-1, 1, 0, 0]
for t in range(int(input())):
    n, m, k = map(int, input().split())
    # print([*map(int,input().split())])
    b = [[*map(int, input().split())] + [0] * k for _ in range(n)] + [[0] * (m + k) for _ in range(k)]
    live = [0] + [[] for _ in range(10)]
    pprint(live)
    pprint(b)