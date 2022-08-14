class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkOutwards(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        res = s[0]
        for i in range(1, len(s)):
            temp = checkOutwards(i-1,i+1)
            if len(temp) > len(res):
                res = temp
            
            temp = checkOutwards(i-1, i)
            if len(temp) > len(res):
                res = temp
        return res