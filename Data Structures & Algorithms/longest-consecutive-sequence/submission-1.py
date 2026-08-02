class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(set(nums))
        max_length=0
        length=1
        if nums==[]:
            return 0
        if len(nums)==1:
            return 1 
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                length+=1
            else:
                max_length=max(max_length,length)
                length=1
        return max(max_length,length)
