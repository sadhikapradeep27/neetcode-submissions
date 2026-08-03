class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_letters={}
        n=len(s1)
        for ch in range(len(s1)):
            s1_letters[s1[ch]]=s1_letters.get(s1[ch],0)+1
        window={}
        l=0
        for r in range(len(s2)):
            window[s2[r]]=window.get(s2[r],0)+1
            if r-l+1>n:
                window[s2[l]]-=1
                if window[s2[l]]==0:
                    del window[s2[l]]
                l+=1
            if window==s1_letters:
                return True
        return False



            