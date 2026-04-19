class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}

        for num in nums:
            if num in nums_map:
                nums_map[num] += 1
            else:
                nums_map[num] = 1
        
        sorted_count = []
        for num, count in nums_map.items():
            sorted_count.append([count, num])
        
        sorted_count.sort()
        print(sorted_count)
        
        top_k = []
        for i in range(k):
            top_k.append(sorted_count.pop()[1])
        
        print(nums_map)
        return top_k
            
            