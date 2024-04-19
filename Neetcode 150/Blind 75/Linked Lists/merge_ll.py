"""

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        head1 = list1
        head2 = list2

        if head1 == None:
            return head2
        elif head2 == None:
            return head1

        if head1.val <= head2.val:
            start = head1
            ptr = head1
            head1 = head1.next
        else:
            start = head2
            ptr = head2
            head2 = head2.next

        while head1 != None or head2 != None:
            if head1 == None:
                ptr.next = head2
                break
            elif head2 == None:
                ptr.next = head1
                break
            elif head1.val <= head2.val:
                ptr.next = head1
                head1 = head1.next

            else:
                ptr.next = head2
                head2 = head2.next
            ptr = ptr.next

        return start


# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

#         """
#         - If any of the list is null return other list
#         - if both list are None return None
#         - if l1 <= l2
#             set l1.next = recurse (l1.next, l2)
#             return l1
#         - else
#             set l2.next = recurse(l1.next, l2.next)
#             return l2
#         """

#         if not list1:
#             return list2
#         elif not list2:
#             return list1

#         if list1.val <= list2.val:
#             # set list1.next -> merged list of (list1.next, list2)
#             list1.next = self.mergeTwoLists(list1.next, list2)
#             return list1
#         else:
#             list2.next = self.mergeTwoLists(list1, list2.next)
#             return list2
