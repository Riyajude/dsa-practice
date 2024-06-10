class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        maxdiff=arr[n-1]-arr[0]
        for i in range(1,n):
            if arr[i]<k:
                continue
            tempmin = min(arr[0] + k, arr[i] - k)
            tempmax = max(arr[i - 1] + k, arr[n - 1] - k)
            maxdiff = min(maxdiff, tempmax - tempmin)
        return maxdiff

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1
