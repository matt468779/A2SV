class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeed = []
        for p, s in zip(position, speed):
            positionSpeed.append([p, s, (target - p)/s])
        
        positionSpeed.sort(reverse=True)
        fleet = 1
        for i in range(len(positionSpeed)-1):
            if positionSpeed[i][2] >= positionSpeed[i+1][2]:
                positionSpeed[i+1][2] = positionSpeed[i][2]
            else:
                fleet += 1

        return fleet