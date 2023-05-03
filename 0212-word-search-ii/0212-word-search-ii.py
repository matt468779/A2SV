class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        n, m = len(board), len(board[0])
        visited, res = set(), set()
        
        def dfs(r, c, node):
            if r >= n or c >= m or r < 0 or c < 0 or board[r][c] not in node.children or (r, c) in visited:
                return
            
            node = node.children[board[r][c]]
            if node.word:
                res.add(node.word)
                
            visited.add((r, c))
            
            dfs(r+1, c, node)
            dfs(r-1, c, node)
            dfs(r, c+1, node)
            dfs(r, c-1, node)
            
            visited.remove((r, c))
            
        for i in range(n):
            for j in range(m):
                dfs(i, j, root)
        return res
    
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
    
    def addWord(self, word):
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        
        cur.word = word