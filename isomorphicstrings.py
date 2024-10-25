class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            # Check if there's a mismatch in the mapping from s to t
            if (char_s in s_to_t and s_to_t[char_s] != char_t) or \
            (char_t in t_to_s and t_to_s[char_t] != char_s):
                return False

            # Set the mapping between characters
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        return True
