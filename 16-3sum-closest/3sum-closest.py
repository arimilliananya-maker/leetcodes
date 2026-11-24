class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest=float('inf')
        ans=0
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while(left<right):
                sum_=nums[i]+nums[left]+nums[right]
                if abs(sum_-target)<closest:
                    closest=abs(sum_-target)
                    ans=sum_
                if sum_<target:
                    left+=1
                elif sum_>target:
                    right-=1
                else:
                    return target
        return ans