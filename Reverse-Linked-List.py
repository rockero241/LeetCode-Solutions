1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
9        prev, curr = None, head
10        while curr:
11            nxt = curr.next
12            curr.next = prev
13            prev = curr
14            curr = nxt
15            
16        return prev