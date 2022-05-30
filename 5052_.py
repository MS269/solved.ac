class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word):
        temp = self.root
        for c in word:
            if c not in temp.children:
                temp.children[c] = Node(c)
            temp = temp.children[c]
        temp.data = word

    def search(self, word):
        temp = self.root
        for c in word:
            if temp.data != None:
                return False
            temp = temp.children[c]
        return True


for _ in range(int(input())):
    n = int(input())
    phones = []
    trie = Trie()
    flag = True

    for _ in range(n):
        phone = input()
        phones.append(phone)
        trie.insert(phone)

    for phone in phones:
        flag &= trie.search(phone)

    print("YES" if flag else "NO")
