class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitude=0
        max_=0
        for i in gain:
            altitude+=i
            max_=max(max_,altitude)
        return max_