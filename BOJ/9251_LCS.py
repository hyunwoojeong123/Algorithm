A = input()
B = input()
N_A = len(A)
N_B = len(B)
# print(A,B,N_A,N_B)
D = [[0 for _ in range(N_B+1)] for _ in range(N_A+1)]

for i in range(1,N_A+1):
    for j in range(1,N_B+1):
        if A[i-1] == B[j-1]:
            D[i][j] = D[i-1][j-1] + 1
        else:
            D[i][j] = max(D[i-1][j],D[i][j-1])
ans = -1
for i in range(1,N_A+1):
    for j in range(1,N_B+1):
        ans = max(D[i][j],ans)

print(ans)