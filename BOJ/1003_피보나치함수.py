
T = int(input())
for _ in range(T):
    N = int(input())
    D_0 = [-1 for _ in range(N+1)]
    D_1 = [-1 for _ in range(N+1)]
    D_0[0] = 1
    D_1[0] = 0
    if N >= 1:
        D_0[1] = 0
        D_1[1] = 1
    for i in range(2,N+1):
        D_0[i] = D_0[i-2] + D_0[i-1]
        D_1[i] = D_1[i-2] + D_1[i-1]
    print(D_0[N],D_1[N])