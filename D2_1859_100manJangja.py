T = int(input())
for i in range(1,T+1):
    n = int(input())
    ret = 0
    price_list = list(map(int,input().split()))
    max_price = price_list[n-1]
    for j in range(n-2,-1,-1):
        if price_list[j] < max_price:
            ret += max_price - price_list[j]
        elif price_list[j] > max_price:
            max_price = price_list[j]
    print(f'#{i} {ret}')

