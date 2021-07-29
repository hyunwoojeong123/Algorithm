N = int(input())

b = [-1 for _ in range(N+1)]
b[0] = 0
b[1] = 1
if N > 1:
    b[2] = 2

for i in range(3,N+1):
    b[i] = b[i-1] + b[i-2]

print(b[N] % 10007)