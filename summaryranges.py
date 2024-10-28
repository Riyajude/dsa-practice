class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges=[]
        n=len(nums)
        if n==0:
            return ranges
        start=nums[0]
        for i in range(1,n):
            if nums[i]!=nums[i-1]+1:
                if start==nums[i-1]:
                    ranges.append(str(start))
                else:
                    ranges.append(str(start)+"->"+str(nums[i-1]))
                start=nums[i]
        if start==nums[-1]:
            ranges.append(str(start))
        else:
                    ranges.append(str(start)+"->"+str(nums[-1]))

        return ranges
