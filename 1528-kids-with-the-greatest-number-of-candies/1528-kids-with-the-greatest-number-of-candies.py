class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a=[]
        b=[]
        for i in range(len(candies)):
            c=candies[i]+extraCandies
            b.append(c)
        m=max(candies)
        for i in range(len(b)):
            if b[i]<m:
                a.append(False)
            else:
                a.append(True)
        return (a)