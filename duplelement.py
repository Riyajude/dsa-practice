class Solution(object):
    def findDuplicate(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return nums[i]
                    break
                



Arr=list(map(int,input()))
ob = Solution()
ans = ob.findDuplicate(Arr)
print(ans)
