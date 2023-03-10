# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge(list1,list2,temp):
            if not list1 and not list2:
                return None
            elif not list1:
                temp.next = list2
                return temp
            elif not list2:
                temp.next = list1
                return temp
            if list1.val < list2.val:
                node = ListNode(list1.val)
                temp.next = node
                temp = temp.next
                merge(list1.next,list2,temp)
            else:
                node = ListNode(list2.val)
                temp.next = node
                temp = temp.next
                merge(list1,list2.next,temp)
            return temp
        dummy = ListNode()
        temp = dummy
        merge(list1,list2,temp)
        return dummy.next