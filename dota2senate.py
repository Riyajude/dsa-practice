class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiantqueue=[]
        direqueue=[]
        n=len(senate)
        for i in range(n):
            if senate[i]=='R':
                radiantqueue.append(i)
            else:
                direqueue.append(i)
        while radiantqueue and direqueue:
            r=radiantqueue.pop(0)
            d=direqueue.pop(0)
            if r<d:
                radiantqueue.append(r+n)
            else:
                direqueue.append(d+n)
        if not radiantqueue:
            return "Dire"
        elif not direqueue:
            return "Radiant"
