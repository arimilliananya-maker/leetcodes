class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        current=1
        max_length=1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                current+=1
                max_length=max(max_length,current)
            else:
                current=1
        return max_length