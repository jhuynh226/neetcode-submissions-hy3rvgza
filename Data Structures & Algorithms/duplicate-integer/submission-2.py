class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Set Solution
        nums_set = set(nums)

        if len(nums) > len(nums_set):
            return True
        else:
            return False

        #Brute Force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        
        # return False

