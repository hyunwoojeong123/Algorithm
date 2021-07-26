import sys

def DFS(state):
    # 만약 arr이 전부 똑같은 색이면 0리턴
    state_arr = state.split(',')
    col = state_arr[0]
    all_same = True
    for i in range(N):
        if state_arr[i] != col:
            all_same = False
            break
    if all_same:
        return 0
    # 만약 D[state]가 있으면 얘 리턴
    if D.get(state,-1) != -1:
        return D[state]
    # 위에서 안 걸러지면 전부 탐색해 최소한의 값으로 간다
    D[state] = INF
    for i in range(N):
        origin = int(state_arr[i])
        for j in range(1,K+1):
            if j == origin:
                continue
            state_arr[i] = str(j)
            next_state = ",".join(state_arr)
            temp = DFS(next_state) + 1
            if temp < D[state]:
                D[state] = temp
            state_arr[i] = str(origin)
    return D[state]

sys.setrecursionlimit(1000000)
INF = sys.maxsize
D = dict()
N,K = map(int,input().split())
arr = input().split()
first_state = ','.join(arr)
print(DFS(first_state))

