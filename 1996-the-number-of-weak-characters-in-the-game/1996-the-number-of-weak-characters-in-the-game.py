class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort()
        nowMax, prevMax = properties[-1][1], float('-inf')
        res = 0
        for i in range(len(properties)-2, -1, -1):
            if properties[i][0] == properties[i+1][0]:
                nowMax = max(nowMax, properties[i][1])
            else:
                prevMax = max(prevMax, nowMax)
                nowMax = properties[i][1]
            if properties[i][1] < prevMax:
                res += 1
                
        return res