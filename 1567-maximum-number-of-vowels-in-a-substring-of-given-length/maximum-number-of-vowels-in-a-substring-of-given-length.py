class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #compute the number of vowels in first
        #k-size meaning 
        vowels="aeiou"
        first_window=s[:k]
        v_c=0
        for i in first_window:
            if i in vowels:
                v_c+=1
        max_v = max(0,v_c)
        #sliding window logic
        for i in range(k,len(s)):
            if s[i] in vowels:
                v_c+=1
            if s[i-k] in vowels:
                v_c-=1
            max_v=max(max_v,v_c)
        return max_v
