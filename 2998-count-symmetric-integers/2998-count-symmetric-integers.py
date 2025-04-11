class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def isSymmetric(num):
            s=str(num)
            if len(s)%2!=0:
                return False
            n=len(s)//2
            return sum(int(d) for d in s[:n])==sum(int(d) for d in s[n:])
        
        count=0
        for i in range(low,high+1):
            if isSymmetric(i):
                count+=1
        return count