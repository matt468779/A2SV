class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        pre_sum = [0] * len(words)
        pre_sum[0] = int(words[0][0] in vowels and words[0][-1] in vowels)
        for i in range(1, len(words)):
            pre_sum[i] = pre_sum[i-1] + int(words[i][0] in vowels and words[i][-1] in vowels)
        
        res = []
        for query in queries:
            if query[0] == 0:
                res.append(pre_sum[query[1]])
            else:
                res.append(pre_sum[query[1]] - pre_sum[query[0]-1])
        
        return res