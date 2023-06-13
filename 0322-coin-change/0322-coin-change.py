class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        changes = [float('inf')] * (amount+1)
        changes[0] = 0
        for i in range(amount+1):
            if changes[i] != float('inf'):
                for coin in coins:
                    if i + coin < len(changes):
                        changes[i+coin] = min(changes[i+coin], 1+changes[i])
        
        return -1 if changes[amount] == float('inf') else changes[amount]