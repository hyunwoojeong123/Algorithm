dx = [0,0,-1,1]
dy = [1,-1,0,0]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    wonjas = []
    for _ in range(N):
        x,y,dir,k = map(int,input().split())
        wonjas.append([x,y,dir,k])
    ans = 0
    while True:
        # 원자 이동
        sz = len(wonjas)
        for i in range(sz):
            wonjas[i][0] += dx[wonjas[i][2]]*0.5
            wonjas[i][1] += dy[wonjas[i][2]]*0.5
            # if wonjas_pos[i][0] < -1000 or wonjas_pos[i][0] > 1000 or wonjas_pos[i][1] < -1000 or wonjas_pos[i][1] > 1000:
            #     wonjas_dead[i] = True
            #     done += 1
        # 원자를 dict에 넣는다.
        pos = dict()
        new_wonjas = []

        for i in range(sz):
            if wonjas[i][0] < -1000 or wonjas[i][0] > 1000 or wonjas[i][1] < -1000 or wonjas[i][1] > 1000:
                continue
            x,y,dir,k = wonjas[i]
            if pos.get((x,y),[]) == []:
                pos[(x,y)] = [[dir,k]]
            else:
                pos[(x,y)].append([dir,k])
        for key in pos:
            if len(pos[key]) > 1:
                for each in pos[key]:
                    ans += each[1]
            else:
                x,y = key
                dir,k = pos[key][0]
                new_wonjas.append([x,y,dir,k])
        wonjas = new_wonjas
        if len(wonjas) <= 1:
            break

    print('#{} {}'.format(tc,ans))