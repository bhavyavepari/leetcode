class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                # Found num > second > first
                return True

        return False
        #for i in range(len(nums)):
         #   for j in range(i+1,len(nums)):
          #      for k in range(i+1,len(nums)):
           #         if(nums[i]<nums[j]) and (nums[j]<nums[k]):
            #            return True
        #return False