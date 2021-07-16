import sys

M = int(input())
S = 0
for _ in range(M):
    cmd = sys.stdin.readline().strip().split()
    # print(cmd)
    x = -1
    if cmd[0] == 'add' or cmd[0] == 'remove' or cmd[0] == 'check' or cmd[0] == 'toggle':
        x = int(cmd[1])-1

    if cmd[0] == 'add':
        S = S | (1 << x)
    elif cmd[0] == 'remove':
        S = S & ~(1 << x)
    elif cmd[0] == 'check':
        if S & (1 << x):
            print(1)
        else:
            print(0)
    elif cmd[0] == 'toggle':
        S = S ^ (1 << x)
    elif cmd[0] == 'all':
        S = (1 << 20) - 1
    elif cmd[0] == 'empty':
        S = 0

# M = int(input())
# S = [False for _ in range(20)]
# for _ in range(M):
#     cmd = input().split()
#     # print(cmd)
#     x = -1
#     if cmd[0] == 'add' or cmd[0] == 'remove' or cmd[0] == 'check' or cmd[0] == 'toggle':
#         x = int(cmd[1])-1
#
#     if cmd[0] == 'add':
#         S[x] = True
#     elif cmd[0] == 'remove':
#         S[x] = False
#     elif cmd[0] == 'check':
#         if S[x]:
#             print(1)
#         else:
#             print(0)
#     elif cmd[0] == 'toggle':
#         if S[x]:
#             S[x] = False
#         else:
#             S[x] = True
#     elif cmd[0] == 'all':
#         for i in range(20):
#             S[i] = True
#     elif cmd[0] == 'empty':
#         for i in range(20):
#             S[i] = False