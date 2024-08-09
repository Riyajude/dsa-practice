class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        left, right = 0,len(s) - 1

        while left < right:
            # Move left pointer to the next vowel
            while left < right and s[left] not in vowels:
                left+= 1
            # Move right pointer to the previous vowel
            while left < right and s[right] not in vowels:
                right-= 1
            
            # If both left and right are pointing to vowels, swap them
            if left<right:
                s[left],s[right]=s[right],s[left]
                left+= 1
                right-= 1

        return ''.join(s)
