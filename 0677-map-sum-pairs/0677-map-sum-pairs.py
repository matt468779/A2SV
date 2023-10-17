class MapSum:

    def __init__(self):
        self.children = {}
        self.val = 0

    def insert(self, key: str, val: int) -> None:
        node = self
        for char in key:
            if char not in node.children:
                node.children[char] = MapSum()
                
            node = node.children[char]
        
        node.val = val

    def sum(self, prefix: str) -> int:
        node = self
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        
        return node.findSum()
    
    def findSum(self) -> int:
        res = 0
        q = deque([self])
        while q:
            popped = q.popleft()
            res += popped.val
            for char in popped.children:
                q.append(popped.children[char])
        
        return res

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)