# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr = []
        dummy = ListNode(0,head)
        count = 0
        leftt = dummy
        curr = ListNode(0)
        while count < left-1:
            count+=1
            leftt = leftt.next
        if leftt.next: 
            curr = leftt.next
        leftt.next = None

        while count < right:
            arr.append(curr.val)
            curr = curr.next
            count+=1
        
        for i in range(len(arr)-1,-1,-1):
            node = ListNode(arr[i])
            leftt.next = node
            leftt = leftt.next
        
        if curr: 
            leftt.next = curr
        return dummy.next