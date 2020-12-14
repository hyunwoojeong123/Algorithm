words = []
while True:
    word = input()
    if word in words:
        break
    words.append(input())