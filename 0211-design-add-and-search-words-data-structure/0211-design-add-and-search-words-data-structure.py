class WordDictionary:

    def __init__(self):
        self.children = {}
        self.isEnd = False
        
    def addWord(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = WordDictionary()
                
            node = node.children[char]
        
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self
        for i in range(len(word)):
            if word[i] == '.':
                for char in node.children:
                    if node.children[char].search(word[i+1:]):
                        return True
                return False
            
            elif word[i] not in node.children:
                return False
        
            node = node.children[word[i]]
            
        return node.isEnd

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)