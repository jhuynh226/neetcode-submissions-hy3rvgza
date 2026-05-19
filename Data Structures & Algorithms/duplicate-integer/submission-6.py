class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #BRUTE FORCE
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        #HASHSET
        nums_set = set() 
        for num in nums:
            if num in nums_set:
                return True
            else:
                nums_set.add(num)

        return False 