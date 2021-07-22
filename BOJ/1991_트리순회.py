def junwi(root):
    if root == '.':
        return ''
    return root+junwi(tree[root][0])+junwi(tree[root][1])
def jungwi(root):
    if root == '.':
        return ''
    return jungwi(tree[root][0]) + root + jungwi(tree[root][1])
def huwi(root):
    if root == '.':
        return ''
    return huwi(tree[root][0]) + huwi(tree[root][1]) + root

tree = dict()
N = int(input())
for _ in range(N):
    me,left,right = input().split()
    tree[me] = [left,right]
# print(tree)
print(junwi('A'))
print(jungwi('A'))
print(huwi('A'))