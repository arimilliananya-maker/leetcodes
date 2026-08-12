class Solution:
    def maxPower(self, s: str) -> int:
        max_length=1
        current=1
        
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                current+=1
                max_length=max(max_length,current)
            else:
                current=1
        return max_length