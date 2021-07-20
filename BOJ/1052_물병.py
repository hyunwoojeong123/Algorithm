N,K = map(int,input().split())
num = N
while True:
    if bin(num).count('1') <= K:
        break
    num += 1
print(num-N)