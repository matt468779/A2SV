class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = min(height[left], height[right]) * (right - left)
        while left < right:
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            temp = min(height[left], height[right]) * (right - left)
            if min(height[left], height[right]) * (right - left) > area:
                area = temp

        return area