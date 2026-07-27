class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        writer = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[writer]=nums[i]
                writer += 1
                k+=1
        return writer
               