class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])):
            currentChar = strs[0][i]
            for j in range(len(strs)):
                if (i >= len(strs[j]) or strs[j][i] != currentChar):
                    return strs[0][:i]
        return strs[0]
        
