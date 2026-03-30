# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # ARRAY SOLUTION O(n) time + space
        # linked_array = []

        # while head:
        #     linked_array.append(head.val)
        #     head = head.next

        # left_pointer, right_pointer = 0, len(linked_array) - 1

        # while left_pointer <= right_pointer:
        #     if linked_array[left_pointer] != linked_array[right_pointer]:
        #         return False
        #     left_pointer += 1
        #     right_pointer -= 1
        
        # return True

        #LINKED SOLUTION O(n) time | O(1) space
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev 
            prev = slow
            slow = next_node

        second_half_head = prev
        while second_half_head:
            if second_half_head.val != head.val:
                return False
            second_half_head = second_half_head.next
            head = head.next
        
        return True
         