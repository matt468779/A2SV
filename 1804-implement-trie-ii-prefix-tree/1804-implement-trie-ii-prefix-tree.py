class Trie:

    def __init__(self):
        self.children = {}
        self.count = 0
        self.downCount = 0
    def insert(self, word: str) -> None:
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = Trie()
            cur = cur.children[char]
            cur.downCount += 1
            
        cur.count += 1
        
    def find(self, word):
        cur = self
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return None
        
        return cur
    def countWordsEqualTo(self, word: str) -> int:
        cur = self.find(word)
        if not cur:
            return 0
        
        return cur.count
    
    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.find(prefix)
        if not cur:
            return 0
        
        return cur.downCount
    
    def erase(self, word: str) -> None:
        cur = self
        for char in word:
            cur = cur.children[char]
            cur.downCount -= 1
            
        cur.count -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)