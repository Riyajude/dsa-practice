class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zerocount=0
        maxlength=0
        left=0
        for right in range(len(nums)):
            if (nums[right]==0):
                zerocount+=1
            while zerocount>k:
                if nums[left]==0:
                    zerocount-=1
                left+=1
            windowsize=right-left+1
            if windowsize>maxlength:
                maxlength=windowsize
        return maxlength

