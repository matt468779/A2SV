class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas]
        [-3, 10, -11, 4]
        
        gasLeft = 0
        start = 0
        prev = 0
        for i in range(len(gas)):
            if gasLeft + gas[i] - cost[i] >= 0:
                gasLeft += gas[i] - cost[i]
            else:
                prev = gasLeft + gas[i] - cost[i]
                gasLeft = 0
                start = (i+1) % len(gas)
        
        for i in range(start):
            if gasLeft + gas[i] - cost[i] >= 0:
                gasLeft += gas[i] - cost[i]
            else:
                return -1
        
        if start == 0 and prev < 0:
            return -1
            
        return start if gasLeft >= 0 else -1