class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        max_length=0
        start=0
        for i in range(len(s)):
            if s[i] in seen and seen[s[i]]>=start:
                start=seen[s[i]]+1
            seen[s[i]]=i
            count = i - start + 1
            max_length = max(max_length, count)
        return max_length
            