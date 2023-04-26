class Trie:
    
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
    def insert(self, word: str) -> None:
        temp = self
        for i in range(len(word)):
            if word[i] in temp.children:
                temp = temp.children[word[i]]
            else:
                node = Trie()
                temp.children[word[i]] = node
                temp = node
                
        temp.isEnd = True
                
    def search(self, word: str) -> bool:
        temp = self
        for i in range(len(word)):
            if word[i] in temp.children:
                temp = temp.children[word[i]]
            else:
                return False
        
        return temp.isEnd

    def startsWith(self, prefix: str) -> bool:
        temp = self
        for i in range(len(prefix)):
            if prefix[i] in temp.children:
                temp = temp.children[prefix[i]]
            else:
                return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)