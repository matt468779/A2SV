class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        
        cur.isWord = True

    def search(self, word, start, res):
        cur = self
        for i in range(start, len(word)):
            if word[i] in cur.children:
                cur = cur.children[word[i]]
                if cur.isWord:
                    res.append([start, i])
            else:
                break
            
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        res = []
        for i in range(len(text)):
            root.search(text, i, res)

        return res



