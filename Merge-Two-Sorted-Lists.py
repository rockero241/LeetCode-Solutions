1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
9        dummy = ListNode()
10        tail = dummy
11
12        while l1 and l2:
13            if l1.val < l2.val:
14                tail.next = l1
15                l1 = l1.next
16            else:
17                tail.next = l2
18                l2 = l2.next
19
20            tail = tail.next
21
22        if l1:
23            tail.next = l1
24        elif l2:
25            tail.next = l2
26
27        return dummy.next