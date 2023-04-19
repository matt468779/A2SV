class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y_presum = [0] * (len(customers)+1)
        for i in range(len(customers)):
            y_presum[i+1] = (customers[i] == 'Y') + y_presum[i]
            
        min_penality = float('inf')
        res = 0
        for i in range(1, len(y_presum)):
            penality = (y_presum[-1] - y_presum[i-1]) + (i-1 - y_presum[i-1])
            if penality < min_penality:
                min_penality = penality
                res = i-1
        
        if len(customers) - y_presum[-1] < min_penality:
            return len(customers)
        return res