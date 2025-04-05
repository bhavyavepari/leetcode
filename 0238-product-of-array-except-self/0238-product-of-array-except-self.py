class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #a=[]
        #for i in range(len(nums)):
         #   p=1
          #  b=nums[i]
           # for j in range(len(nums)):
            #    if i!=j:
             #       p*=nums[j]
            #a.append(p)
        #return a
        n = len(nums)
        answer = [1] * n
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer