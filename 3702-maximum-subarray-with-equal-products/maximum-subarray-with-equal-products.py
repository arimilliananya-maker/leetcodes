class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans=0
        import math
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                arr=nums[i:j+1]
                prod=1
                g=arr[0]
                l=arr[0]
                for i in range(len(arr)):
                    prod*=arr[i]
                    g=math.gcd(g,arr[i])
                    l=math.lcm(l,arr[i])
                if prod==l*g:
                    ans=max(ans,len(arr))
        return ans