"""

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

"""


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        curr_node = head
        fast_node = head
        slow_node = head
        while fast_node and fast_node.next:
            fast_node = fast_node.next.next
            slow_node = slow_node.next

        def reverse_list(node):
            prev_node = None
            while node:
                next_node = node.next
                node.next = prev_node
                prev_node = node
                node = next_node

            return prev_node

        second_half = reverse_list(slow_node)
        while curr_node and second_half.next:
            tmp1 = curr_node.next
            tmp2 = second_half.next
            curr_node.next = second_half
            second_half.next = tmp1
            curr_node = tmp1
            second_half = tmp2
