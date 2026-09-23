class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output=[]
        s=0
        for i in nums:
            s+=i
            output.append(s)
        return output