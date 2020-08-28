# N*N 보드에 각 행에 한 놈만 배치하는데 열이 다르게 해서 배치한다.
# 그다음 대각선만 체크해주면 된다.
N = -1
hangs = []
ans = 0

#공격 받는지,안받는지 체크
def check(i):
    for j in range(0,i):
        if hangs[i] == hangs[j] or abs(hangs[i]-hangs[j]) == i-j:
            return False
    return True

# 말을 어떻게 배치할까
def NQueen(i):
    if i == N:
        global ans
        ans += 1
    else:
        for j in range(0,N):
            hangs[i] = j
            if check(i):
                NQueen(i+1)
        

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    hangs = [-1 for x in range(0,N)]
    ans = 0
    NQueen(0)

    print(f'#{tc} {ans}')

