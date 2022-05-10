class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeed = []
        for p, s in zip(position, speed):
            positionSpeed.append([p, (target - p)/s])
        
        positionSpeed.sort(reverse=True)
        fleet = 1
        for i in range(len(positionSpeed)-1):
            if positionSpeed[i][1] >= positionSpeed[i+1][1]:
                positionSpeed[i+1][1] = positionSpeed[i][1]
            else:
                fleet += 1

        return fleet