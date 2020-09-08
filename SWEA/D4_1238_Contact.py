import sys
sys.stdin = open("input.txt","r")
from pprint import pprint

for tc in range(1,11):
    N, start = list(map(int,input().split()))
    link_input = list(map(int,input().split()))
    link_list = [[False for j in range(101)] for i in range(101)]
    for i in range(0,N,2):
        a,b = link_input[i],link_input[i+1]
        link_list[a][b] = True
    q = []
    visited = [False for _ in range(101)]
    visited[start] = True
    q.append([start,0])
    #print(q)
    ans,ans_idx = start,0
    while q:
        ls = q.pop(0)
        node, idx = ls[0],ls[1]
        #print(node,idx)
        if ans_idx < idx:
            ans = node
            ans_idx = idx
        if ans_idx == idx:
            #print(node,ans,'ans_idx == idx')
            if node > ans:
                #print('{} = {}'.format(ans,node))
                ans = node
        #print(node,idx)
        #print(node)
        for k in range(1,101):
            if link_list[node][k] and not visited[k]:
                visited[k] = True
                q.append([k,idx+1])

    print('#{} {}'.format(tc,ans))
