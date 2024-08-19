#sliding window
#2 variables cursum and maxavg
#iterate till window size and get cursum and avg
#iterate for remaining elements from k, increment cursum with value of nums[i] and decrement nums[i-k], take avg of cursum and calculate maxavg as max of present maxavg and avg
#return maxavg

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        cursum=0
        for i in range(k):
            cursum+=nums[i]
        maxavg=cursum/k
        for i in range(k,n):
            cursum+=nums[i]
            cursum-=nums[i-k]

            avg=cursum/k
            maxavg=max(maxavg,avg)
        return maxavg
