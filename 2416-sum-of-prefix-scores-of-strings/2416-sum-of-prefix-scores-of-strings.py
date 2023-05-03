class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.add(word)
        
        res = [0] * len(words)
        for i in range(len(words)):
            cur = trie
            for char in words[i]:
                res[i] += cur.children[char].score
                cur = cur.children[char]
                
        return res
    
class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.score = 1
    
    def add(self, word):
        cur = self
        for char in word:
            if char in cur.children:
                cur.children[char].score += 1
            else:
                temp = Trie()
                cur.children[char] = temp
                
            cur = cur.children[char]
        cur.isEnd = True
    