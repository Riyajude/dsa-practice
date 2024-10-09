
class Solution:
    def findsqr(self, n:int):
        sum=0
        while n!=0:
            d=n%10
            sum=sum+d**2
            n=n//10
        return sum

    def isHappy(self, n: int) -> bool:
        seen = set()  # to detect cycles
        while n != 1 and n not in seen:
            seen.add(n)  # keep track of visited numbers
            n = self.findsqr(n)  # call the method using self

        return n == 1
