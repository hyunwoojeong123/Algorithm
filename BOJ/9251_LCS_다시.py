A = input()
B = input()
N_A = len(A)
N_B = len(B)
ans = 0
D = [[0 for _ in range(N_B+1)] for _ in range(N_A+1)]
for i in range(0,N_A):
    for j in range(0,N_B):
        if A[i] == B[j]:
            D[i+1][j+1] = D[i][j] + 1
        else:
            D[i+1][j+1] = max(D[i][j+1],D[i+1][j])
        ans = max(D[i+1][j+1],ans)

print(ans)
