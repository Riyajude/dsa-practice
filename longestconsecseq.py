class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        left,right=1,1
        
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]: 
                if i>0 and (nums[i]==nums[i-1]+1):
                    right=right+1
                else:
                    left = max(left, right)
                    right=1
                    
        
        return max(left,right)
