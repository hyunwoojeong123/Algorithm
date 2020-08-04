import sys
sys.stdin = open("input.txt","r")

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
    arr = [False for x in range(200)]
    checked = [False for x in range(len(students))]
    count = 0
    t = 0
    while True:
        t += 1
        #print(f'{t}초 지남')
        arr = [False for x in range(200)]
        for i in range(len(students)):
            if checked[i]:
                continue
            student = students[i]
            start,end = student[0],student[1]
            start,end = change(start),change(end)
            #print(f'{i}번째 학생 {start},{end}')
            cant = False
            for j in range(start,end+1):
                if arr[j]:
                    cant = True
                    break
            if cant:
                continue
            else:
                for j in range(start,end+1):
                    arr[j] = True
                count += 1
                checked[i] = True
                #print(f'{i}번째 학생 집감')
        if count == len(students):
            break
    print(f'#{tc} {t}')