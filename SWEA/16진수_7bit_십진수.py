arr = ['0','F','9','7','A','3']
dict = {'0' : '0000' , '1' : '0001', '2' : '0010' , '3' : '0011', '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111', '8' : '1000', '9' : '1001', 'A' : '1010', 'B' : '1011',
        'C' : '1100', 'D' : '1101', 'E' : '1110', 'F' : '1111'}

binstr = ''
for each in arr:
    binstr += dict[each]

for i in range(0,len(binstr),7):
    num = 0
    v = 1
    for each in binstr[i:i+7][::-1]:
        if each == '1':
            num += v
        v *= 2
    print(num)
