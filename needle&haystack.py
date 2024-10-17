class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haylen=len(haystack)
        needlelen=len(needle)
        if needlelen==0:
            return 0
        if haylen<needlelen:
            return -1
        for i in range(haylen-needlelen+1):
            window = haystack[i:i+needlelen]
            if window==needle:
                return i
        return -1
