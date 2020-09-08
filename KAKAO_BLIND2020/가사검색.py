class Node(object):
    def __init__(self,key,flag = False):
        self.key = key
        self.flag = flag
        self.children = {}
        self.lengthLeft = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self,string):
        curr_node = self.head
        leftlen = len(string)
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            if curr_node.lengthLeft.get(leftlen,0) == 0:
                curr_node.lengthLeft[leftlen] = 1
            else:
                curr_node.lengthLeft[leftlen] += 1
            leftlen -= 1
            curr_node = curr_node.children[char]
        curr_node.flag = True

    def starts_with(self,prefix,leftlen):
        curr_node = self.head
        result = 0
        subtrie = None
        for char in prefix:
            if char in curr_node.children:
                #print(curr_node.key,curr_node.lengthLeft)
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return 0
        #print(curr_node.key,curr_node.lengthLeft)
        result = curr_node.lengthLeft.get(leftlen,0)
        return result

#ords = ['frodo', 'front', 'frost', 'frozen', 'frame','kakao']
#queries = ['fro??', '????o', 'fr???', 'fro???', 'pro?']

def solution(words,queries):
    answer = []
    right = Trie()
    rev = Trie()
    # 단어 넣음.
    for word in words:
        right.insert(word)
        rev.insert(word[::-1])
    # 검색
    for query in queries:
        #print(query,'실행')
        is_rev = False
        if query[0] == '?':
            # 역방향
            is_rev = True
            query = query[::-1]
            #print(query,'로 변환')
        qm_cnt = 0
        for char in query:
            if char == '?':
                qm_cnt += 1
        if is_rev:
            res = rev.starts_with(query[0:-qm_cnt],qm_cnt)
        else:
            res = right.starts_with(query[0:-qm_cnt], qm_cnt)
        answer.append(res)

    return answer

#print(solution(words,queries))