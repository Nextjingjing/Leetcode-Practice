from typing import Optional

# comment this class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        numberL1 = self.listToNumberInverse(l1)
        numberL2 = self.listToNumberInverse(l2)

        result = numberL1 + numberL2

        return self.numberToListInverse(result)
    
    def listToNumberInverse(self, linkList):
        resultNumber = 0
        multiplier = 1

        helperNode = linkList
        while helperNode is not None:
            resultNumber += helperNode.val * multiplier
            multiplier *= 10
            helperNode = helperNode.next
        return resultNumber
    
    def numberToListInverse(self, number):
        if number == 0:
            return ListNode(0)
        
        head = None
        current = None
        
        while number > 0:
            digit = number % 10
            number //= 10
            
            newNode = ListNode(digit)
            if head is None:
                head = newNode
                current = head
            else:
                current.next = newNode
                current = current.next
        
        return head