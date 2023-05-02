class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            trie.add(word)
            
        res = []
        cur = trie
        while cur.children and not cur.isEnd:
            char = list(cur.children.keys())[0]
            res.append(char)
            cur = cur.children[char]
        return ''.join(res)


class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
    def add(self, word):
        cur  = self
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            elif len(cur.children) == 0:
                temp = Trie()
                cur.children[char] = temp
                cur = temp
            else:
                break
        cur.isEnd = True