class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted = []
        for char in s:
            if char.isnumeric():
                converted.append(char)
            elif char.isalpha():
                converted.append(char.lower())
        
        for i in range(len(converted)//2):
            if converted[i] != converted[-i-1]:
                return False
        
        return True
