class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt=[]
        val=0
        alt.append(val)
        for i in range(len(gain)):
            val=val+gain[i]
            alt.append(val)
        return max(alt)
