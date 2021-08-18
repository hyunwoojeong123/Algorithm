def solution(numbers, hand):
    ans = ''
    lu, ru = [3, 0], [3, 2]
    pos = dict()
    pos[1] = [0, 0]
    pos[2] = [0, 1]
    pos[3] = [0, 2]
    pos[4] = [1, 0]
    pos[5] = [1, 1]
    pos[6] = [1, 2]
    pos[7] = [2, 0]
    pos[8] = [2, 1]
    pos[9] = [2, 2]
    pos[0] = [3, 1]

    def dist(A, B):
        return abs(A[0] - B[0]) + abs(A[1] - B[1])

    for number in numbers:
        if number in [1, 4, 7]:
            lu = pos[number]
            ans += 'L'
        elif number in [3, 6, 9]:
            ru = pos[number]
            ans += 'R'
        else:
            # print(dist(lu,pos[number]), dist(ru,pos[number]))
            if dist(lu, pos[number]) < dist(ru, pos[number]):
                lu = pos[number]
                ans += 'L'
            elif dist(lu, pos[number]) > dist(ru, pos[number]):
                ru = pos[number]
                ans += 'R'
            else:
                if hand == 'left':
                    lu = pos[number]
                    ans += 'L'
                else:
                    ru = pos[number]
                    ans += 'R'

    return ans