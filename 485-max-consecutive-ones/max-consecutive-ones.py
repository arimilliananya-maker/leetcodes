class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        one_count=0
        max_count=0
        for i in nums:
            if i==1:
                one_count+=1
                max_count=max(max_count,one_count)
            elif i==0:
                one_count=0
        return max_count
