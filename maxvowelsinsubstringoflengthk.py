class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a','e','i','o','u']
        maxv=0
        currv=0
        for i in range(k):
            if s[i] in vowels:
                currv+=1
        maxv=currv
        for i in range(k,len(s)):
            if s[i-k] in vowels:
                currv=currv-1
            if s[i] in vowels:
                currv+=1
            maxv=max(maxv,currv)
        return maxv
