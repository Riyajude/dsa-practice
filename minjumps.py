class Solution:
	def minJumps(self, arr, n):
	    if (n<=1):
	        return 0
	    if (arr[0]==0):
	        return -1
	    maxrange=arr[0]
	    jumps=1
	    steps=arr[0]
	    for i in range(1,n):
	        if (i == n - 1): 
	            return jumps
	        maxrange = max(maxrange,i+arr[i])
	        steps-=1
	        if (steps == 0):
	            jumps+=1
	            if(i>=maxrange):
	                return -1
                steps= maxrange - i

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
