class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        count = 1
        res, start = 0, 0
        for i in range(1, len(word)):
            if word[i] > word[i-1]:
                count += 1
            if word[i] < word[i-1]:
                start = i
                count = 1
            
            if count == 5:
                res = max(res, i-start+1)
        
        return res
            