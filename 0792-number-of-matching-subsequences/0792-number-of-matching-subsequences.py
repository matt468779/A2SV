class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.count = 0
        
    def addWord(self, word):
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        
        cur.count += 1
        cur.isEnd = True
            
            
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        cur = TrieNode()
        for word in words:
            cur.addWord(word)
        
        res = 0
        q = deque([(char, trieNode, 0) for char, trieNode in cur.children.items()])
        while q:
            l = len(q)
            for _ in range(l):
                popChar, popTrie, start = q.popleft()
                ind = s.find(popChar, start)
                
                if ind == -1:
                    continue
                if popTrie.isEnd:
                    res += popTrie.count
                    
                for char, trieNode in popTrie.children.items():
                    q.append((char, trieNode, ind+1))
        
        return res