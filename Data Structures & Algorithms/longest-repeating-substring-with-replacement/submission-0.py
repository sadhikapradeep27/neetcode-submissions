class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        max_length=0
        max_fre=0
        l=0
        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1
            max_fre=max(count[s[r]],max_fre)

            window=r-l+1

            if window-max_fre>k:
                count[s[l]]-=1
                l+=1
            max_length=max(max_length,r-l+1)
        return max_length
            
