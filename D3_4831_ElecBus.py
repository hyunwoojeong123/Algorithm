# 최대한 간 다음 충전기 있으면, 거기서 멈춤.
# 없으면, 한칸 뒤로
# 이거 반복

T = int(input())
for tc in range(1,T+1):
    K, N, M = list(map(int,input().split()))
    chargers = list(map(int,input().split()))
    visited = [False for x in range(N+1)]
    charge_cnt = 0
    pos = 0
    while pos < N:
        if visited[pos]:
            charge_cnt = 0
            break
        visited[pos] = True
        pos += K
        if pos >= N:
            break
        #print(f'{pos}로 이동')
        if pos in chargers:
            charge_cnt += 1
            #print(f'{pos}에서 충전')
        else:
            while not(pos in chargers):
                pos -= 1
            #print(f'{pos}로 이동, 충전')
            charge_cnt += 1
    print(f'#{tc} {charge_cnt}')