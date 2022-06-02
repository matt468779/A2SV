class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if time == 0:
            return range(len(security))
        
        before = [0] * len(security)
        after = [0] * len(security)
        i = 1
        j = len(security)-2
        while i < len(security)-1:
            if security[i] <= security[i-1]:
                before[i] = before[i-1] + 1
            if security[j] <= security[j+1]:
                after[j] = after[j+1] + 1
            i += 1
            j -= 1
        
        res = []
        for i in range(time, len(security)-time):
            if before[i] >= time and after[i] >= time:
                res.append(i)
        return res
            