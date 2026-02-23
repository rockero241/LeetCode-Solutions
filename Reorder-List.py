1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def reorderList(self, head: Optional[ListNode]) -> None:
9        slow, fast = head, head.next
10        while fast and fast.next:
11            slow = slow.next
12            fast = fast.next.next
13
14        second = slow.next
15        prev = slow.next = None
16        while second:
17            tmp = second.next
18            second.next = prev
19            prev = second
20            second = tmp
21
22        first, second = head, prev
23        while second:
24            tmp1, tmp2 = first.next, second.next
25            first.next = second
26            second.next = tmp1
27            first, second = tmp1, tmp2