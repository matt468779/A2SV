class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindrome(word):
            for i in range(len(word)//2):
                if word[i] != word[-i-1]:
                    return False
            return True
        
        for word in words:
            if is_palindrome(word):
                return word
        
        return ''