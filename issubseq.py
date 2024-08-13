class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sindex=tindex=0
        while sindex<len(s) and tindex<len(t):
            if s[sindex]==t[tindex]:
                sindex+=1
            tindex+=1
        return sindex==len(s)
