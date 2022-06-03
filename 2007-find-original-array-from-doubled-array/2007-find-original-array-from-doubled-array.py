class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        changed.sort()
        j = 1
        res = []
        for i in range(len(changed)):
            if changed[i] == -1:
                continue
            if j <= i:
                j = i+1
            while j < len(changed) and changed[j] != 2 * changed[i]:
                j += 1
            if j == len(changed):
                return []
            
            changed[j] = -1
            res.append(changed[i])
            j += 1
          
        return res