class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        curr = self.left.next
        while curr and index > 0 and curr!=self.right:
            curr = curr.next
            index-=1
        if index == 0 and curr != self.right:
            return curr.val
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be
        the first node of the linked list.
        """
        node= ListNode(val)
        node.next = self.left.next
        self.left.next = node
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        lastNode = self.left
        while lastNode and lastNode.next != self.right:
            lastNode = lastNode.next
        node = ListNode(val)
        lastNode.next = node
        node.next = self.right
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked
        list, the node will be appended to the end of linked list. If index is greater than the length, the node will not
        be inserted.
        """
        node = ListNode(val)
        curr = self.left
        while curr and index > 0:
            curr = curr.next
            index-=1
        if curr and index == 0:
            node.next = curr.next
            curr.next = node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        delNode = self.left
        while delNode and delNode.next != self.right and index > 0:
            delNode = delNode.next
            index-=1
        if delNode and index==0 and delNode.next!=self.right:
            delNode.next = delNode.next.next
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)