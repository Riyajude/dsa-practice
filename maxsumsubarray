class Solution:
    
    def maxSubArraySum(self, arr, n):
       max_ending_here = 0
       max_so_far = -999
       for i in range(0, n):
           max_ending_here = max_ending_here + arr[i]
           if max_so_far < max_ending_here:
               max_so_far = max_ending_here
           if max_ending_here < 0:
               max_ending_here = 0
       return max_so_far
     
import math

def main():
    T = int(input())
    while (T > 0):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
