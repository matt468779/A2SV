class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre_xor = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            pre_xor[i+1] = pre_xor[i] ^ arr[i]
        
        res = []
        for query in queries:
            res.append(pre_xor[query[0]] ^ pre_xor[query[1]+1])
        
        return res