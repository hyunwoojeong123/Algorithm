T = int(input())
for i in range(1,T+1):
    Tnum = input()
    scores = list(map(int,input().split()))
    most_count = 0
    most_score = 0
    for st_score in range(0,101):
        cnt = 0
        for score in scores:
            if st_score == score:
                cnt += 1
        if cnt >= most_count:
            most_count = cnt
            most_score = st_score
    
    print(f'#{Tnum} {most_score}')