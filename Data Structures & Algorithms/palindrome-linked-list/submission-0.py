# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        linked_array = []

        while head:
            linked_array.append(head.val)
            head = head.next

        left_pointer, right_pointer = 0, len(linked_array) - 1

        while left_pointer <= right_pointer:
            if linked_array[left_pointer] != linked_array[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1
        
        return True
            