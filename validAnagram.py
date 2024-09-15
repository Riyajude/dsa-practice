#either check if both the sorted strings are same or check using a manual counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        #return sorted(s)==sorted(t)
        count = [0] * 26  # Assume only lowercase English letters
    
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for c in count:
            if c != 0:
                return False
        
        return True
