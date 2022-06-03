class Solution:
    def countVowels(self, word: str) -> int:
        count = 0
        l = len(word)
        for i in range(l):
            if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u':
                count += (l-i)*(i+1)
        return count
        
        
        
        