# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode()
        currDummy = dummy
        temp = head
        while temp:
            if temp.val < x:
                node = ListNode(temp.val)
                if dummy.next == None:
                    dummy.next = node
                    currDummy = node
                else:
                    currDummy.next = node
                    currDummy = currDummy.next
            temp = temp.next
        temp = head
        while temp:
            if temp.val >= x:
                node = ListNode(temp.val)
                if dummy.next == None:
                    dummy.next = node
                    currDummy = node
                else:
                    currDummy.next = node
                    currDummy = currDummy.next
            temp = temp.next
                    
        return dummy.next