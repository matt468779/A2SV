class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.initColor = image[sr][sc]
        self.finalColor = color
        self.floodFillHelper(image, sr, sc)
        return image
    
    def floodFillHelper(self, image:List[List[int]], sr: int, sc: int):
        if sr > -1 and sr < len(image) and sc > -1 and sc < len(image[0]) and image[sr][sc] == self.initColor and image[sr][sc] != self.finalColor:
            image[sr][sc] = self.finalColor
            self.floodFillHelper(image, sr+1, sc)
            self.floodFillHelper(image, sr, sc+1)
            self.floodFillHelper(image, sr-1, sc)
            self.floodFillHelper(image, sr, sc-1)