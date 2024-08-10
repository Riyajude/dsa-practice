#Left Product Pass:
#left_product starts at 1, and the array answer is populated with the cumulative product of elements to the left of each index.
#For example, after the first pass, answer[i] contains the product of all elements to the left of index i.

#Right Product Pass:
#right_product starts at 1, and the array answer is updated by multiplying it with the cumulative product of elements to the right of each index.
#After this pass, answer[i] will contain the product of all elements in the array except nums[i].

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        

        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer
        
