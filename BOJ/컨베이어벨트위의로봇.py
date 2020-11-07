N,K = map(int,input().split())
naegudos = list(map(int,input().split()))
robots = []
step = 1
# 0 올라가는 위치 N-1 내려가는 위치
while True:
    # 1. 벨트 한칸 회전
    naegudos.insert(0,naegudos.pop())
    for i in range(len(robots)):
        robots[i] = (robots[i]+1)%(2*N)
    # 내릴 로봇 있으면 내림
    if N-1 in robots:
        robots.remove(N-1)
    # 2. 로봇이 움직일 수 있으면 이동
    rbs = len(robots)
    for i in range(rbs):
        if (robots[i]+1)%(2*N) not in robots and naegudos[(robots[i]+1)%(2*N)] > 0:
            robots[i] = (robots[i]+1)%(2*N)
            naegudos[robots[i]] -= 1
    # 내릴 로봇 있으면 내림
    if N-1 in robots:
        robots.remove(N-1)
    # 로봇 올림
    if 0 not in robots and naegudos[0] > 0:
        robots.append(0)
        naegudos[0] -= 1
    if naegudos.count(0) >= K:
        break
    step += 1
print(step)
