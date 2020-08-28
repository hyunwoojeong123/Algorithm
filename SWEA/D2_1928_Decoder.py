ref = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def changeDecto6Bin(num):
    res = ''
    for i in range(5):
        mod = num % 2
        num = num // 2
        res = str(mod) + res
        if i == 4:
            res = str(num) + res
    return res


def changeStrTo6Bin(sentence):
    res = ''
    for char in sentence:
        num = ref.find(char)
        res += changeDecto6Bin(num)
    return res

def change8bToStr(b8):
    asc = 0
    n = 2**7
    for i in range(8):
        if b8[i] == '1':
           asc += n
        n //= 2
    return chr(asc) 

def changeBinsToStr(Bins):
    res = ''
    reps = len(Bins)//8
    for rep in range(reps):
        res += change8bToStr(Bins[rep*8:rep*8+8])
    return res
    


T = int(input())
for tc in range(1,T+1):
    sentence = input()
    binary = changeStrTo6Bin(sentence)
    ans = changeBinsToStr(binary)
    print(f'#{tc} {ans}')
    
