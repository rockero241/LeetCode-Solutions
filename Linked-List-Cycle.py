1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        slow, fast = head, head
10        while fast and fast.next:
11            slow = slow.next
12            fast = fast.next.next
13
14            if slow == fast:
15                return True
16
17        return False