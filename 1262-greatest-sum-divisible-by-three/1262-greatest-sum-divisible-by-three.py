class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        res = sum(nums)
        if res % 3 == 0:
            return res
        
        remain = res % 3
        heapq.heapify(nums)
        ones = []
        twos = []
        while nums:
            num = heapq.heappop(nums)
            if remain == 1:
                if len(ones) < 1 and num%3 == 1:
                    ones.append(num)
                elif len(twos) < 2 and num%3 == 2:
                    twos.append(num)
                
                if len(ones) == 1 and len(twos) == 2:
                    return max(res-ones[0], res-sum(twos))
                
            elif remain == 2:
                if not twos and num%3 == 2:
                    twos.append(num)
                elif len(ones) < 2 and num%3 == 1:
                    ones.append(num)
                
                if len(ones) == 2 and len(twos) == 1:
                    return max(res-twos[0], res-sum(ones))

        if remain == 1 and ones:
            return res - ones[0]
        elif remain == 1 and twos:
            return res - sum(twos)
        elif remain == 2 and twos:
            return res - twos[0]
        elif remain == 2 and ones:
            return res - sum(ones)
            
        return 0