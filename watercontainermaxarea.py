#initialise 2 pointers left at 0 and right at lenght-1
#iterate as long as left<right
#calculate current area as min value of element at left and right multiplied with the width=right-left
#calculate actual area as max value of area and current area
#if element at left<right then increment left, else decrement right, Finally return area

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        area=0
        while left<right:
            currarea=min(height[left], height[right])*(right-left)
            area=max(area,currarea)
            if height[left]<height[right]:
                left+= 1
            else:
                right-= 1
    
        return area
