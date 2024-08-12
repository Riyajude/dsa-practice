#traverse list and search for non zero numbers and overwrite list from starting as non0 number and update lastnon0.
#after all non zero elements overwritter, overwrite rest of elements of list as 0

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lastnon0=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[lastnon0]=nums[i]
                lastnon0+=1
        for i in range(lastnon0,len(nums)):
            nums[i]=0
        return nums
        
