

for t in range(1,11):
    number = int(input())
    buildings = list(map(int,input().split()))
    result = 0
    for i in range(2,number-2):
        max_height = max(buildings[i-2],buildings[i-1],buildings[i+1],buildings[i+2])
        if max_height < buildings[i]:
            result += buildings[i] - max_height
    print(f'#{t} {result}')