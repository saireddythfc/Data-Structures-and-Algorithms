"""

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

"""


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return None
        elif head.next == None:
            if n > 0:
                return None

        prev = head
        curr = head

        size = 0

        while curr:
            size += 1
            curr = curr.next

        curr = head

        i = 0
        while i < size - n:
            prev = curr
            curr = curr.next
            i += 1

        if curr == head:
            return head.next
        else:
            prev.next = curr.next

        return head
