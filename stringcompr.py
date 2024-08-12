#traverse list as long as i<n and curr char matches list element-->increment count. 
#Overwrite chars[index] with curr char. if count is >1, convert each digit of count as character and overwrite in list.
#return final value of index as the length of overwritten section of array

class Solution:
    def compress(self, chars: List[str]) -> int:
        n=len(chars)
        index=i=0
        while i<n:
            curr=chars[i]
            count=0
            while (i<n and chars[i]==curr):
                count+=1
                i=i+1
            chars[index]=curr
            index+=1
            if count>1:
                for digit in str(count):
                    chars[index] = digit
                    index += 1
        return index

        
