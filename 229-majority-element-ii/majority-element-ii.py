class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        d={}
        ans=[]
        for i in nums:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        for key,value in d.items():
            if value>len(nums)//3:
                ans.append(key)
        return ans