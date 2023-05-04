class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        root = TrieNode()
        for i in range(len(products)):
            root.addWord(products[i], i)
        
        return root.search(searchWord, products)
            
class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []
    
    def addWord(self, word, ind):
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
            if len(cur.words) < 3:
                cur.words.append(word)
    
    def search(self, key, words):
        res = [[] for _ in range(len(key))]
        cur = self
        for i in range(len(key)):
            if key[i] in cur.children:
                res[i] = cur.children[key[i]].words
            else:
                break
            cur = cur.children[key[i]]
        
        return res