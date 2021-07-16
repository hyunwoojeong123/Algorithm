# 64짜리 막대기를 자르고 붙여서 X로 만듬
# 막대기들 합이 X보다 크면 아래 과정 반복
# 막대기중 젤 짧은거를 절반으로 짜름
# 남은 막대 길이합이

X = int(input())
# X = 3
# print( X & (1 << 0))
answer = 0
for i in range(7):
    if X & (1 << i):
        answer += 1

print(answer)

