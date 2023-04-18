# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reverse(head):
            prev = head
            curr = head.next
            if curr and head.next.next:
                nextt = head.next.next
                while nextt:
                    curr.next = prev
                    prev = curr
                    curr = nextt
                    nextt = nextt.next
                curr.next = prev
                head.next = None
                return curr
            else:
                if curr:
                    curr.next = prev
                    head.next = None
                    return curr
                else:
                    return head

        def calculate(head1,head2):
            res = 0
            while head2:
                res = max(res, head1.val + head2.val)
                head1 = head1.next
                head2 = head2.next
            return res

        r = reverse(slow)
        return calculate(head,r)