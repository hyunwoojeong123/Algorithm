def jinbub(number,n):
    ans = ''
    while number // n >= 1:
        print(number)
        remain = number % n
        number = number // n
        ans = str(remain) + ans
        if number < n:
            ans = str(number) + ans
        return ans
        

print(jinbub(10,2))
