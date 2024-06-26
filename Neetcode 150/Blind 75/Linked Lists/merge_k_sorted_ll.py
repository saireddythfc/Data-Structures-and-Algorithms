"""

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.


Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

"""


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []
        for ll in lists:
            if ll == None:
                continue
            curr = ll
            while curr:
                vals.append(curr.val)
                curr = curr.next

        vals.sort()
        head = ListNode(0)
        chain = head
        for value in vals:
            curr = ListNode(value)
            chain.next = curr
            chain = chain.next

        return head.next
