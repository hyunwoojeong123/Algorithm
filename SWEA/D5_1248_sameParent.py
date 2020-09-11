def count_subtree(root):
    #print(root)
    if len(children[root]) == 0:
        return 1
    elif len(children[root]) == 1:
        return 1+count_subtree(children[root][0])
    else:
        return 1+count_subtree(children[root][0]) + count_subtree(children[root][1])


def all_ansc(i):
    res = []
    while parents[i]:
        res.append(parents[i])
        i = parents[i]
    return res

def find_same_ansc(A_anscs,B_anscs):
    for A_ansc in A_anscs:
        for B_ansc in B_anscs:
            if A_ansc == B_ansc:
                return A_ansc

T = int(input())
for tc in range(1,T+1):
    V,E,A,B = list(map(int,input().split()))
    parents = [0 for _ in range(V+1)]
    children = [[] for _ in range(V+1)]
    elements = list(map(int,input().split()))
    for i in range(0,len(elements),2):
        parent,son = elements[i],elements[i+1]
        #print(parent,son)
        children[parent].append(son)
        parents[son] = parent
    #print(V,E,A,B,parents)
    A_anscs,B_anscs = all_ansc(A),all_ansc(B)
    #print(A_anscs,B_anscs)
    same_ansc = find_same_ansc(A_anscs,B_anscs)
    print('#{} {} {}'.format(tc,same_ansc,count_subtree(same_ansc)))