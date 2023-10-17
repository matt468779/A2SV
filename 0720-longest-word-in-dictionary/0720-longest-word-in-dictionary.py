class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: (len(x), x))
        root = TrieNode()
        res = ""
        for word in words:
            if root.addWord(word) and len(res) < len(word):
                res = word
        
        return res
    
class TrieNode:
    def __init__(self):
        self.children = {}
    
    def addWord(self, word) -> bool:
        node = self
        for i in range(len(word)-1):
            if word[i] not in node.children:
                return False
            node = node.children[word[i]]
        
        node.children[word[-1]] = TrieNode()
        return True