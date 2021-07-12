# 10:47~11:08
def solution(places):
    answer = []
    N = 5
    def dist(A,B):
        return abs(A[0]-B[0])+abs(A[1]-B[1])
    for place in places:
        # print('장소 1개 검색!')
        is_right = True
        waitings = []
        for i in range(N):
            for j in range(N):
                if place[i][j] == 'P':
                    waitings.append([i,j])
        for i in range(len(waitings)):
            for j in range(i+1,len(waitings)):
                D = dist(waitings[i],waitings[j])
                if D < 2:
                    is_right=False
                    break
                elif D == 2:
                    # 세로 일렬로 서잇는 경우
                    if waitings[i][0]==waitings[j][0]:
                        ii = waitings[i][0]
                        jj = (waitings[i][1]+waitings[j][1])//2
                        if place[ii][jj] == 'X':
                            continue
                        else:
                            is_right=False
                            break
                    # 가로 일렬
                    elif waitings[i][1]==waitings[j][1]:
                        ii = (waitings[i][0]+waitings[j][0])//2
                        jj = waitings[i][1]
                        if place[ii][jj] == 'X':
                            continue
                        else:
                            is_right=False
                            break
                    # 대각선으로 서잇는 경우
                    else:
                        ii1= waitings[i][0]
                        ii2= waitings[j][0]
                        jj1= waitings[j][1]
                        jj2= waitings[i][1]
                        if place[ii1][jj1] == 'X' and place[ii2][jj2] == 'X':
                            continue
                        else:
                            is_right=False
                            break
                else:
                    continue
        if is_right:
            answer.append(1)
        else:
            answer.append(0)
        # print('후에', answer)
    return answer