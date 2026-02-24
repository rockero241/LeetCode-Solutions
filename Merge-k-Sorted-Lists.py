1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:    
8    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
9        if not lists or len(lists) == 0:
10            return None
11
12        while len(lists) > 1:
13            mergedLists = []
14
15            for i in range(0, len(lists), 2):
16                l1 = lists[i]
17                l2 = lists[i + 1] if (i + 1) < len(lists) else None
18                mergedLists.append(self.mergeList(l1, l2))
19            lists = mergedLists
20        return lists[0]
21
22    def mergeList(self, l1, l2):
23        dummy = ListNode()
24        tail = dummy
25
26        while l1 and l2:
27            if l1.val < l2.val:
28                tail.next = l1
29                l1 = l1.next
30            else:
31                tail.next = l2
32                l2 = l2.next
33
34            tail = tail.next
35
36        if l1:
37            tail.next = l1
38        elif l2:
39            tail.next = l2
40
41        return dummy.next