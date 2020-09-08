def rotate(num,dir):
    # print('rotate({},{})'.format(num,dir))
    rotated[num] = True
    left_num, right_num = num-1, num+1
    # 먼저 양 옆 겹치는 부분을 체크해서 돌림, rotated이면 안 돌림
    # 딴 색깔 설정
    opp_dir = -1
    if dir == -1:
        opp_dir = 1
    # 왼쪽 먼저 체크
    if left_num > 0 and not rotated[left_num] and tobnis[num][6] != tobnis[left_num][2]:
        rotate(left_num,opp_dir)
    # 오른쪽 체크
    if right_num < 5 and not rotated[right_num] and tobnis[num][2] != tobnis[right_num][6]:
        rotate(right_num,opp_dir)

    # 톱니를 해당 방향으로 돌린다.
    changed = [-1 for _ in range(8)]
    if dir == -1:
        for i in range(0,7):
            changed[i] = tobnis[num][i+1]
        changed[7] = tobnis[num][0]
    else:
        for i in range(1,8):
            changed[i] = tobnis[num][i-1]
        changed[0] = tobnis[num][7]
    for i in range(8):
        tobnis[num][i] = changed[i]
tobnis = [[0]]

for _ in range(4):
    temp = input()
    tobni = []
    for each in temp:
        tobni.append(int(each))
    tobnis.append(tobni)

# for i in range(1, 5):
    # print(tobnis[i])

K = int(input())
for _ in range(K):
    num,dir = list(map(int,input().split()))
    rotated = [False for _ in range(5)]
    rotate(num,dir)
    # for i in range(1, 5):
    #     print(tobnis[i])

ans = 0
val = 1
for i in range(1,5):
    if tobnis[i][0]:
        ans += val
    val *= 2
print(ans)