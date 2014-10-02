# Definition for singly-linked list.
class ListNode:
    # def __init__(self, x):
    #     self.val = x
    #     self.next = None
    def __init__(self, x=None, nextNode=None):
        self.val = x
        self.next = nextNode

    def __repr__(self):
        result = []
        current = self
        while current is not None:
            result.append(current.val)
            current = current.next

        return str(result)


class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head): # head = 1 -> 2 -> 3
        # corner cases
        if head is None or head.next is None:
            return head
        
        # split the list into two lists
        slow, fast, prev = head, head, None # slow = 1, fast = 1, prev = None
        while fast is not None and fast.next is not None:
            prev = slow 
            slow = slow.next 
            fast = fast.next.next
        prev.next = None

        # print(slow)
        # print(head)
        
        # reverse the second list
        prev = None
        while slow.next is not None: # slow = 2 -> 3 -> None
            tmp = slow.next # tmp = 3
            slow.next = prev # prev = None <- 2 = slow tmp = 3 -> None
            prev = slow # None <- 2 = prev 
            slow = tmp # None <- 2 = prev slow = 3 -> None
        slow.next = prev
        # print(slow)

        # merge two lists
        dummyNode = ListNode(0, None)
        current = dummyNode
        while slow is not None and head is not None:
            current.next = head
            current = head
            head = head.next
            
            current.next = slow
            current = slow
            slow = slow.next

        if head is not None:
            current.next = head
        if slow is not None:
            current.next = slow
            
        return dummyNode.next


def convert(nodeVals):
    nodeVals.reverse()    
    preNode = None
    for nodeVal in nodeVals:
        newNode = ListNode(nodeVal, preNode)
        preNode = newNode
    return preNode

vals = [1, 2, 3]
# print(convert(vals))

# current = convert(vals)
# while current is not None:
    # print(current)
    # current = current.next

print(Solution().reorderList(convert(vals)))


            
        