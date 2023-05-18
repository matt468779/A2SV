class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def findState(word):
            state = 0
            for char in word:
                mask = 2**(ord(char) - ord('a'))
                if not mask & state:
                    state |= mask
            
            return state
        
        res = 0
        states = [findState(word) for word in words]
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not states[i] & states[j]:
                    product = len(words[i]) * len(words[j])
                    res = max(res, product)
        
        return res