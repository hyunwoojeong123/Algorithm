def cnt_subtree(node):
    if len(childs[node]) == 0:
        return 1
    elif len(childs[node]) == 1:
        return 1+cnt_subtree(childs[node][0])
    else:
        return 1+cnt_subtree(childs[node][0])+cnt_subtree(childs[node][1])

T = int(input())
for tc in range(1,T+1):
    V,E,A,B = list(map(int,input().split()))
    elements = list(map(int,input().split()))
    childs = [[] for _ in range(V+1)]
    parent = [0 for _ in range(V+1)]
    for i in range(0,len(elements),2):
        p,c = elements[i],elements[i+1]
        childs[p].append(c)
        parent[c] = p
    pa,pb = parent[A],parent[B]
    A_ansc, B_ansc = [], []
    while pa != 0:
        A_ansc.append(pa)
        pa = parent[pa]
    while pb != 0:
        B_ansc.append(pb)
        pb = parent[pb]
    flag = False
    for aansc in A_ansc:
        for bbnsc in B_ansc:
            if aansc == bbnsc:
                print('#{} {} {}'.format(tc,aansc, cnt_subtree(aansc)))
                flag = True
                break
        if flag:
            break
