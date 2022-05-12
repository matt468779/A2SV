import collections as c

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        counts = c.Counter(nums)
        uniqueNums = sorted(counts.keys())
        increments = 0
        isIndexLast = False
        if len(uniqueNums) > 1:
            left, right = uniqueNums[0], uniqueNums[1]
            lIndex, rIndex = 0, 1

        else:
            left, right = uniqueNums[0], inf
            isIndexLast = True
        i = 0
        for num in uniqueNums:
            notUnique = counts[num] - 1
            if left < num:
                if rIndex < len(uniqueNums)-1:
                    lIndex = i
                    rIndex = i+1
                    left, right = uniqueNums[lIndex], uniqueNums[rIndex]
                elif rIndex >= len(uniqueNums)-1:
                    right = inf
                    if left < uniqueNums[-1]:
                        left = uniqueNums[-1]
                    isIndexLast = True
            while notUnique >= 1:
                while right - left > 1 and notUnique >= 1:
                    left += 1
                    notUnique -= 1
                    increments += left - num
                
                if not isIndexLast and right - left <= 1 :
                    if rIndex < len(uniqueNums)-1:
                        lIndex += 1
                        rIndex += 1
                        left, right = uniqueNums[lIndex], uniqueNums[rIndex]
                    elif rIndex >= len(uniqueNums)-1:
                        right = inf
                        left = uniqueNums[-1]
                        isIndexLast = True
            i+=1

        return increments