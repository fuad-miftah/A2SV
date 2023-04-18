# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def check(head1,head2):
            if not head2:
                return True
            if head1.val != head2.val:
                return False
            return check(head1.next,head2.next)

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
                    
        #print(slow)
        r = reverse(slow)
        return check(head,r)