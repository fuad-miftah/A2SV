# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap, gidx = [], 0
        
        for head in lists:
            if head:
                heapq.heappush(min_heap, (head.val, gidx, head))
                gidx += 1
        
        dummy_head = ListNode(0)
        t_head = dummy_head
        while min_heap:
            v, ind, node = heapq.heappop(min_heap)
            if node.next:
                heapq.heappush(min_heap, (node.next.val, gidx, node.next))
                gidx += 1
            node.next = None
            t_head.next = node
            t_head = t_head.next
        return dummy_head.next