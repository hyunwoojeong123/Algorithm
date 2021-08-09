def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return len(cities)*5
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            for i in range(len(cache)):
                if cache[i] == city:
                    cache.pop(i)
                    break
            cache.append(city)
        else:
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city)
            answer += 5
        # print(city,'를 반영한후 캐시',cache)
    return answer