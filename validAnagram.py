#either check if both the sorted strings are same or check using a manual counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        #return sorted(s)==sorted(t)
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in t:
            if i in d:
                d[i]-=1
            else:
                return False
        for i in d:
            if d[i]!=0:
                return False
            return True
