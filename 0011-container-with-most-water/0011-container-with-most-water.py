class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l=0
        r=n-1
        w=0
        while(l<r):
            if height[l]<=height[r]:
                res=height[l]*(r-l)
                l+=1
            else:
                res=height[r]*(r-l)
                r-=1
            if res>w:
                w=res
        return w
