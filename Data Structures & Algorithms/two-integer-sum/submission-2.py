class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        #Hash Map
        prev_values = {}
        for i in range(len(nums)):
            desired_value = target - nums[i]
            if desired_value in prev_values:
                return [prev_values[desired_value], i]

            prev_values[nums[i]] = i