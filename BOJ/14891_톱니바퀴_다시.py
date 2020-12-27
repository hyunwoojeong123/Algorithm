# 톱니바퀴 회전 함수
# 회전시키기 전 맞닿은 애들 확인.
# 맞닿은 애들 서로 다르면 걔는 반대방향으로 회전
# 왼쪽, 오른쪽으로 각각 회전 전파 시킨다고 생각하자.

# 1 : 시계 -1 : 반시계
# 톱니 배열에서 0 번째 애가 12시방향
reverse = {1: -1, -1:1}

def rotate(num,dir):
    # print('rotate({},{})'.format(num,dir))
    rotated[num] = True
    left = num-1
    right = num+1
    if left >= 0 and left <= 3 and not rotated[left]:
        if topnis[left][2] != topnis[num][6]:
            rotate(left, reverse[dir])
    if right >= 0 and right <= 3 and not rotated[right]:
        if topnis[right][6] != topnis[num][2]:
            rotate(right, reverse[dir])
    if dir == 1:
        item = topnis[num].pop()
        topnis[num].insert(0,item)
    else:
        item = topnis[num].pop(0)
        topnis[num].append(item)

topnis = []
for _ in range(4):
    ips = input()
    topnis.append(list(map(int,list(ips))))
k = int(input())
for _ in range(k):
    num,dir = map(int,input().split())
    rotated = [False for _ in range(4)]
    rotate(num-1,dir)
    # print(topnis)
ans = 0
for _ in range(4):
    if topnis[_][0]:
        ans += 2**_
print(ans)


