class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        words_d = {w: i for i, w in enumerate(words)}
        ans = []

        for i in range(n):
		
            # 1, words[i]=='' check: are there palindromes among other words?
            if not words[i]:  
                for j in range(n):
                    if i != j and self.check_palindrome(words[j]):
                        ans += [[j, i], [i, j]]

            # 2 check: reversed word in other words?
            bw, l_w = words[i][::-1], len(words[i])  # reversed word
            if bw in words_d and words_d[bw] != i:  
                ans.append([i, words_d[bw]])

            # 3 check **and**: 
            # 1) part (suffix or prefix) of reversed word in words? 
            # 2) the rest of reversed word is a palindrome?
            for j in range(1, l_w): 

                for k in range(2):
                                    # suffix if k else prefix
                    bwj, l, r = (bw[j:], 0, j - 1) if k else (bw[:j], j, l_w - 1)

                    if bwj in words_d and self.check_palindrome(bw, l, r):
                        ans += [[i, words_d[bwj]]] if k else [[words_d[bwj], i]]

        return ans

    def check_palindrome(self, word: str, i: int = 0, j: int = None):
        j = j if j is not None else len(word) - 1

        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1

        return True