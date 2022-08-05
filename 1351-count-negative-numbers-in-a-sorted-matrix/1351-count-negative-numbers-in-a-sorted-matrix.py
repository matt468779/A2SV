class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        loX, loY = 0, 0
        hiX, hiY = len(grid[0])-1, len(grid)-1
        res = 0
        boundX, boundY = len(grid[0]), len(grid)
        while hiX >= 0 and hiY >= 0 and grid[hiY][hiX] < 0:
            while loY < hiY:
                mid = (loY + hiY)//2
                if grid[mid][boundX-1] < 0:
                    hiY = mid
                else:
                    loY = mid+1
            tempLoX = 0
            tempHiX = boundX-1
            while tempLoX < tempHiX:
                mid = (tempLoX + tempHiX)//2
                if grid[loY][mid] < 0:
                    tempHiX = mid
                else:
                    tempLoX = mid+1
            
            while loX < hiX:
                mid = (loX + hiX)//2
                if grid[boundY-1][mid] < 0:
                    hiX = mid
                else:
                    loX = mid+1
            tempLoY = 0
            tempHiY = boundY-1
            while tempLoY < tempHiY:
                mid = (tempLoY + tempHiY)//2
                if grid[mid][loX] < 0:
                    tempHiY = mid
                else:
                    tempLoY = mid+1
            
            res += (boundY-loY) * (boundX-tempLoX) + (boundX-loX)*(boundY-tempLoY)
            res -= (boundY-tempLoY) * (boundX-tempLoX)
            loX, loY = 0, 0
            hiX, hiY = tempLoX-1, tempLoY-1
            boundX, boundY = tempLoX, tempLoY
            
        return res   