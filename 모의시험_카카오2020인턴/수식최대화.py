def solution(expression):
    answer = 0
    tp = ''
    opers = []
    prior = dict()
    prior['+'], prior['-'], prior['*'] = -1, -1, -1

    for each in expression:
        if each.isdigit():
            tp += each
        else:
            opers.append(int(tp))
            tp = ''
            opers.append(each)
    opers.append(int(tp))

    ## 경우의수 전부
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            for k in range(3):
                if j == k or i == k:
                    continue
                prior['+'] = i
                prior['-'] = j
                prior['*'] = k

                ## 우선순위대로 연산

                # 후위 표기식으로 변환 후 연산
                huwi = []
                st = []
                for oper in opers[::-1]:
                    if oper in ['*', '-', '+']:
                        if st == []:
                            st.append(oper)
                        else:
                            while st != [] and prior[st[-1]] < prior[oper]:
                                huwi.append(st.pop())
                            st.append(oper)
                    else:
                        huwi.append(oper)
                while st != []:
                    huwi.append(st.pop())

                print(huwi)
                print(prior)
                st = []
                for each in huwi:
                    if each in ['*', '-', '+']:
                        A = st.pop()
                        B = st.pop()
                        if each == '*':
                            st.append(A * B)
                        elif each == '-':
                            st.append(A - B)
                        elif each == '+':
                            st.append(A + B)
                    else:
                        st.append(each)
                    print(st)
                res = abs(st.pop())
                answer = max(res, answer)

    return answer