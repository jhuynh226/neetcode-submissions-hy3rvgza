# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        intermediate_states = []

        if pairs:
            intermediate_states.append(pairs[:])

        for i in range(1, len(pairs)):
            j = i - 1

            while j >= 0 and pairs[j + 1].key < pairs[j].key:
               current = pairs[j + 1]
               pairs[j + 1] = pairs[j] 
               pairs[j] = current
               j -= 1

            intermediate_states.append(pairs[:])
            
        
        return intermediate_states

        