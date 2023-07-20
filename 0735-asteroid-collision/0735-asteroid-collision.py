class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        right = []
        prev = 0
        for i in range(len(asteroids)):
            if asteroids[i] < 0:
                while right and right[-1] < -asteroids[i]:
                    right.pop()
                if not right:
                    res.append(asteroids[i])
                elif right[-1] == -asteroids[i]:
                    right.pop()
            else:
                right.append(asteroids[i])
        
        return res+right