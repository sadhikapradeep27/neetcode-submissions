class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for i in range(len(nums)):
            remaining=target-nums[i]
            if remaining in s:
                return [s[remaining],i]
            s[nums[i]]=i
            