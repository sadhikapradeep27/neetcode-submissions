class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums=sorted(nums)
        result=[]
        
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
        
            j=i+1
            r=n-1
            while j<r:
                total=nums[i]+nums[j]+nums[r]
                if total==0:
                    result.append([nums[i],nums[j],nums[r]])
                    j+=1
                    r-=1
                    while j<r and nums[j]==nums[j-1]:
                        j+=1
                    while j<r and nums[r]==nums[r+1]:
                        r-=1
                elif total<0:
                    j+=1
                else:
                    r-=1
            
        return result
