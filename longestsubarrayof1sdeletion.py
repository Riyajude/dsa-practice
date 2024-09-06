class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zerocount = 0
        maxlength = 0
        left = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zerocount += 1
            
            while zerocount > 1:
                if nums[left] == 0:
                    zerocount -= 1
                left += 1  
            maxlength = max(maxlength, right - left)
        
        return maxlength
