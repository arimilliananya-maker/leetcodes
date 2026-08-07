class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_count=0
        left=0
        right=0
        maxLength=0
        for right in range(len(nums)):
            if nums[right]==0:
                zero_count+=1
            #find invalid state until valid shrink
            while zero_count>k:
                #shrink()
                if nums[left]==0:
                    zero_count-=1
                left+=1
            #update maxLength
            maxLength=max(maxLength,right-left+1)
        return maxLength
            

