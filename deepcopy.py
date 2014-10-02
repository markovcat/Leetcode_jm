# Definition for singly-linked list with a random pointer.
class RandomListNode:
    # def __init__(self, x):
    #     self.label = x
    #     self.next = None
    #     self.random = None

# Definition for singly-linked list.
# class ListNode:
    # def __init__(self, x):
    #     self.val = x
    #     self.next = None
    def __init__(self, x=None, nextNode=None):
        self.label = x
        self.next = nextNode
        self.random = nextNode

    def __repr__(self):
        result = []
        current = self
        while current is not None:
            result.append(current.label)
            current = current.next

        return str(result)

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        # corner case
        if head is None:
            return None
            
        if head.next is None:
            newHead = RandomListNode(head.label)
            if head.random is head:
                newHead.random = newHead
            return newHead
            
        # insert a new node after each original node
        current = head
        while current is not None:
            newHead = RandomListNode(current.label)
            newHead.next = current.next
            current.next = newHead
            current = current.next.next
        
        print(head)

        # copy random pointer for each new node
        prev = head
        current = head.next
        while current.next is not None: 
            if prev.random is not None:
                current.random = prev.random.next
            prev = prev.next.next
            current = current.next.next

        print(head)
        
        # split the new list into two lists
        newHead = head.next
        list1, list2 = head, head.next
        while list2.next is not None:
            list1.next = list2.next
            list2.next = list1.next.next
            list1 = list1.next
            list2 = list2.next
        list1.next = None
        
        print(newHead)
        print(head)

        return newHead

vals = [1, 2, 3]

def convert(nodeVals):
    nodeVals.reverse()    
    preNode = None
    for nodeVal in nodeVals:
        newNode = RandomListNode(nodeVal, preNode)
        preNode = newNode
    return preNode

print(Solution().copyRandomList(convert(vals)))