class Solution:
    def numSplits(self, s: str) -> int:
        distinct_right = [0] * len(s)
        distinct_left = [0] * len(s) 
        left_set, right_set = set(), set()
        for i in range(len(s)):
            left_set.add(s[i])
            right_set.add(s[-i-1])
            
            distinct_left[i] = len(left_set)
            distinct_right[-i-1] = len(right_set)
        
        res = 0
        for i in range(len(s)-1):
            res += distinct_left[i] == distinct_right[i+1]
        
        return res