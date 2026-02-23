1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
9        dummy = ListNode(0, head)
10        left = dummy
11        right = head
12
13        while n > 0 and right:
14            right = right.next
15            n -= 1
16
17        while right:
18            left = left.next
19            right = right.next
20
21        left.next = left.next.next
22        return dummy.next