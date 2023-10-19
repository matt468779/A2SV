class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()
        temp = 1 << 31

        for num in nums:
            root.addNum(num, temp)
        
        res = 0
        for num in nums:
            res = max(res, root.findMaxXOR(num, temp))
        
        return res
    
class TrieNode:
    def __init__(self):
        self.children = {}
    
    def addNum(self, num, mask):
        node = self.children
        while mask:
            bit = bool(mask & num)
            if bit not in node:
                node[bit] = {}
                
            node = node[bit]
            mask >>= 1
    
    def findMaxXOR(self, num, mask):
        node = self.children
        res = 0
        while mask:
            bit = bool(mask & num)
            invertedBit = not bit
            if invertedBit in node:
                node = node[invertedBit]
                res += mask
            else:
                node = node[bit]
            
            mask >>= 1
        
        return res