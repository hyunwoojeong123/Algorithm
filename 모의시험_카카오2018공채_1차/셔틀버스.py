def solution(n, t, m, timetable):
    def changeTime(time):
        h, m = map(int, time.split(":"))
        return 60 * h + m

    def changeStr(time):
        h = time // 60
        m = time % 60
        h = str(h)
        m = str(m)
        if int(h) < 10:
            h = '0' + h
        if int(m) < 10:
            m = '0' + m
        return h + ":" + m

    N = len(timetable)
    timetable.sort(key=lambda x: changeTime(x))
    # print(timetable)
    answer = ''

    first_dochak = changeTime("09:00")
    is_gone = [False for _ in range(N)]
    taeums, dochaks = [], []
    for d in range(n):
        dochak = first_dochak + t * d
        dochaks.append(dochak)
        taeum = []
        cnt = 0
        for i in range(N):
            if is_gone[i]:
                continue
            time = changeTime(timetable[i])
            if time <= dochak:
                taeum.append(timetable[i])
                cnt += 1
                is_gone[i] = True
            if cnt >= m:
                break
        taeums.append(taeum)
    # print(taeums)
    #     뒤에서부터 태울수 있는지 볼건데
    # 만약 인원이 다 차있지 않으면 버스도착시간이 정답
    # 만약 인원이 다 차 있으면 젤늦게 도착한넘보다 1분빠르게 타면댐
    answer = -1
    for i in range(len(taeums))[::-1]:
        # print(taeums[i])
        if len(taeums[i]) < m:
            answer = max(answer, dochaks[i])
        else:
            late_men = -1
            for each in taeums[i]:
                late_men = max(late_men, changeTime(each))
            # print(late_men)
            answer = max(answer, late_men - 1)
    answer = changeStr(answer)
    return answer