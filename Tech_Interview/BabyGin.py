# nums = [4,5,6,7,7,7]
# cnt = [0 for _ in range(10)]
# for num in nums:
#     cnt[num] += 1
#
# run = False
# triple = False
# # 똑같은게 3이상인지 체크
# for i in range(10):
#     if cnt[i] >= 3:
#         run = True
#         cnt[i] -= 3
#
# # 연속으로 3개 숫자가 있는지 체크
# for i in range(8):
#     if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1:
#         triple = True
#         cnt[i] -= 1
#         cnt[i+1] -= 1
#         cnt[i+2] -= 1
#
# if run and triple:
#     print('베이비진!')
# else:
#     print('ㄴㄴ')
