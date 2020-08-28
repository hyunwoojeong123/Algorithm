# import sys
# sys.stdin = open("input.txt","r")

def change(loc):
    if loc % 2 == 0:
        return loc // 2 - 1
    else:
        return loc // 2

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    students = [list(map(int,input().split())) for i in range(N)]
    # std[1]이 std[0]보다 큰 경우는 바꿔주자.
    for student in students:
        if student[1] < student[0]:
            student[0],student[1] = student[1], student[0]
    dist = [0 for x in range(200)]
    for student in students:
        start = change(student[0])
        end = change(student[1])
        for i in range(start,end+1):
            dist[i] += 1
    ans = -1
    for i in range(len(dist)):
        ans = max(ans,dist[i])

    print(f'#{tc} {ans}')