N = int(input())
A = list(map(int,input().split()))
B,C = list(map(int,input().split()))
# N: 시험장 개수, A: 각 방의 응시자 수 배열
# B : 총감독관이 감독할 수 있는 인원수 C: 부감독관이 감독할 수 있는 인원수
# 각 방에 총감독관을 넣는다.
# 그 외에는 다 부감독관으로 채운다.

# 각 방에 총감독관이 감독할 수 있는 인원수만큼 뺴주고, ans는 + 해준다.
ans = 0
for i in range(N):
    ans += 1
    A[i] -= B
    if A[i] < 0:
        A[i] = 0

for i in range(N):
    if A[i] == 0:
        continue
    ans += A[i]//C
    if A[i] % C > 0:
        ans += 1
print(ans)
