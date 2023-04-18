# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next and head.next.next:
            startEven = head.next
            evenCurr = startEven
            evenNext = startEven.next.next
            oddCurr = head
            oddNext = head.next.next
            while oddNext:
                oddCurr.next = oddNext
                oddCurr = oddNext
                if oddNext.next and oddNext.next.next:
                    oddNext = oddNext.next.next
                else:
                    oddNext = None
                if evenNext:
                    evenCurr.next = evenNext
                    evenCurr = evenNext
                    if evenNext.next and evenNext.next.next:
                        evenNext = evenNext.next.next
                    else:
                        evenNext = None
            oddCurr.next = startEven
            evenCurr.next = None
            return head
        else:
            return head