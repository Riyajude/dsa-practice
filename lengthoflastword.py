class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length=0
        flag=False
        l=len(s)
        for i in range(l-1,-1,-1):
            if s[i]!=' ':
                flag=True
                length=length+1
            elif flag:
                break
        return length
        
        
        
