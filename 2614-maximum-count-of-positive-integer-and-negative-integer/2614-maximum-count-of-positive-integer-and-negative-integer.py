class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positive_count=0
        negative_count=0
        for i in nums:
            if(i>0):
                positive_count+=1
            elif(i<0):
                negative_count+=1
        if(negative_count>positive_count):
            return negative_count
        else:
            return positive_count
        
        