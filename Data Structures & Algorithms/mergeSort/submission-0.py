# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def mergeSortHelper(arr, start, end):
            if end - start + 1 <= 1:
                return arr
    
            middle = (start + end) // 2
    
            mergeSortHelper(arr, start, middle)
            mergeSortHelper(arr, middle + 1, end)
            merge(arr, start, middle, end)
        
            return arr
        
        def merge(arr, start, middle, end):
            left_half = arr[start : middle + 1]
            right_half = arr[middle + 1 : end + 1]
    
            i = 0
            j = 0
            k = start
    
            while i < len(left_half) and j < len(right_half):
                if left_half[i].key <= right_half[j].key:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                
                k += 1
    
            while i < len(left_half):
                arr[k] = left_half[i]
                k += 1
                i += 1
            while j < len(right_half):
                arr[k] = right_half[j]
                k += 1
                j += 1

        return mergeSortHelper(pairs, 0, len(pairs) - 1)
