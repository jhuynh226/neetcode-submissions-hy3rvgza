class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #iterate through nums
        #if nums[i] == val
        #for i in range(i + 1, len):
        #nums[i] = nums[i + 1]
        #k = len(nums) k-=1
        k = len(nums)
        i = 0

        while i < k:
            if nums[i] == val:
                for j in range(i + 1, len(nums)):
                    nums[j - 1] = nums[j]
                
                k -= 1
            
            else:
                i += 1

        
        return k
                
