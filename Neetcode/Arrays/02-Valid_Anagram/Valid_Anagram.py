class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        counter_s = {}
        counter_t = {}

        for char in s:
            counter_s[char] = counter_s.get(char, 0) + 1

        for char in t:
            counter_t[char] = counter_t.get(char, 0) + 1

        return counter_s == counter_t

