class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1
    
    def add(self, word, i):
        node = self
        for j in range(len(word)):
            if word[j] == "#":
                break
            if word[j] not in node.children:
                node.children[word[j]] = TrieNode()
            node = node.children[word[j]]
        
        for k in range(j, len(word)):
            if word[k] not in node.children:
                node.children[word[k]] = TrieNode()
            node.index = i
            node = node.children[word[k]]
        node.index = i
    
    def find(self, word):
        node = self
        for char in word:
            if char not in node.children:
                return -1
            
            node = node.children[char]
        
        return node.index

class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for i in range(len(words)):
            for j in range(len(words[i])+1):
                self.root.add(words[i][j:]+"#"+words[i], i)
        
    def f(self, pref: str, suff: str) -> int:
        
        return self.root.find(suff+"#"+pref)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)