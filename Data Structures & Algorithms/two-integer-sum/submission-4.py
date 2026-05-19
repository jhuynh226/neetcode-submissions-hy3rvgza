class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1 2 3 4      T=5

        # BRUTE O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        #HASHMAP
        nums_map = {}

        for i in range(len(nums)):
            desired_num = target - nums[i]
            if desired_num in nums_map:
                return [nums_map[desired_num], i]
            else:
                nums_map[nums[i]] = i