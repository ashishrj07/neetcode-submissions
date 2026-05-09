class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count=1
        for i in nums:
            if nums.count(i)>1:
                count+=1
        return count!=1


        