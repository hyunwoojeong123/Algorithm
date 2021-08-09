
def solution(lines):
    answer = 0
    def changeTime(time):
        h,m,s = time.split(":")
        return int((float(h) * 3600 + float(m) * 60 + float(s))*1000)
    times = []
    for line in lines:
        date,time,duration = line.split()
        duration = int(float(duration[:-1]) * 1000)
        ed = changeTime(time)
        st = ed - duration + 1
        times.append([st,ed])
    def check(t):
        # print(t,'체크')
        cnt = 0
        st = t
        ed = t + 1000
        for time in times:
            if time[0] < st and time[1] < st:
                pass
            elif time[0] >= ed and time[1] >= ed:
                pass
            else:
                cnt += 1
        return cnt
    for time in times:
        answer = max(answer, check(time[0]))
        answer = max(answer, check(time[1]))
    return answer