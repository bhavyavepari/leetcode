class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while(k>0):
            a=nums.pop()
            nums.insert(0,a)
            k-=1
        
        