T = int(input())
for tc in range(1,T+1):
    N,M = list(map(int,input().split()))
    cheeses = list(map(int,input().split()))
    pizzas = []
    hwaduk = []
    for i in range(M):
        pizzas.append([i+1,cheeses[i]])
    for _ in range(N):
        hwaduk.append(pizzas.pop(0))
    cnt = M
    while cnt > 1:
        pizza = hwaduk.pop(0)
        pizza[1] //= 2
        if pizza[1] != 0:
            hwaduk.append(pizza)
        else:
            cnt -= 1
            if pizzas:
                hwaduk.append(pizzas.pop(0))
    ans = -1
    if hwaduk:
        ans = hwaduk[0][0]
    else:
        ans = pizzas[0][0]
    print('#{} {}'.format(tc,ans))


