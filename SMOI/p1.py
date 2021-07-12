def DFS(cnt):
    global ans
    if cnt == len(persons):
        # print(go_exit)
        # 언제 도착하느지 먼저 보자
        dochaks = [[] for _ in range(2)]
        for k in range(len(persons)):
            exit_num = go_exit[k]
            exit_pos = exits[exit_num]
            my_pos = persons[k]
            dist = abs(exit_pos[0]-my_pos[0]) + abs(exit_pos[1]-my_pos[1])
            dochaks[exit_num].append(dist)

        for k in range(2):
            dochaks[k] = sorted(dochaks[k])
        # print(dochaks)
        last_out = [0,0]
        for k in range(2):
        #     각 출구에서 마지막으로 언제 나가는지
            for each in dochaks[k]:
                if each <= last_out[k]:
                    last_out[k] += 1
                else:
                    last_out[k] = each+1
        # print(max(last_out))
        if ans > max(last_out):
            ans = max(last_out)
        return
    for k in range(2):
        go_exit[cnt] = k
        DFS(cnt+1)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 987654321
    exits = []
    persons = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                persons.append([i,j])
            elif arr[i][j] == 2:
                exits.append([i,j])
    # print(persons,exits)
    go_exit = [-1 for _ in range(len(persons))]
    # print(go_exit)
    DFS(0)
    print('#{} {}'.format(tc,ans))