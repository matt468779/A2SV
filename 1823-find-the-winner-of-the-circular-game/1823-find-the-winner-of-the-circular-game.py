class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n+1))
        return self.findTheWin(friends, 0, k)
    
    def findTheWin(self, friends: List[int], next: int, k:int) -> int:
        if len(friends) == 1:
            return friends[0]
        next = (next + k % len(friends) - 1) % len(friends)
        friends.pop(next)
        return self.findTheWin(friends, next, k)