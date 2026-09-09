class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_position=bisect.bisect_left(nums,target)
        last_position=bisect.bisect_right(nums,target)
        if first_position!=last_position:
            return [first_position,last_position-1]
        else:
            return [-1,-1]