class Solution:
    def romanToInt(self, s: str) -> int:
        romanvalues = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000}
        total = 0
        n = len(s)
        for i in range(n):
            currentvalue = romanvalues[s[i]]

            if i < n - 1 and romanvalues[s[i]] < romanvalues[s[i + 1]]:
                total -= currentvalue
            else:
                total += currentvalue
        
        return total
