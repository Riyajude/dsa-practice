#Calculate GCD of Lengths: Compute the greatest common divisor (GCD) of the lengths of str1 and str2. This gives the length of the largest possible common divisor string.
#Extract Candidate Substring: Extract the substring of str1 that has the length equal to the GCD calculated in step 1. This substring is our candidate.
#Verify Divisibility: Check if this candidate substring can divide both str1 and str2. A string x divides another string s if repeating x enough times results in s.
#Return Result: If the candidate substring divides both str1 and str2, return it. Otherwise, return an empty string.


class Solution:
    def commondivisor(self,a,b):
        while b:
            a,b=b,a%b
        return a
    def isdiv(self,mainstr,substr,ln):
        return substr*ln==mainstr
        
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ln1=len(str1)
        ln2=len(str2)
        i=self.commondivisor(ln1,ln2)
        substr=str1[:i]
        if self.isdiv(str1,substr,int(ln1/i)) and self.isdiv(str2, substr, int(ln2/i)):
            return substr
        return ''
