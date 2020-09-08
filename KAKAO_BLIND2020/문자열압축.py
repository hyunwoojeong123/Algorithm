def solution(s):
    answer = len(s)
    N = len(s)
    for length in range(1, N // 2 + 1):
        parts = []
        for i in range(0, N, length):
            parts.append(s[i:i+length])
        print(parts)
        plen = len(parts)
        cnt = 0
        i = 0
        visited = [False for _ in range(plen)]
        for i in range(plen):
            if visited[i]:
                continue
            visited[i] = True
            cnt += len(parts[i])
            repeated = False
            for j in range(i+1,plen):
                if parts[i] == parts[j]:
                    visited[j] = True
                    repeated = True
                else:
                    break
            if repeated:
                cnt += 1
        if answer > cnt:
            answer = cnt
    return answer

print(solution('a'*1000))