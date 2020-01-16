#Submitted-1, wrong answer in case sum > 10
#Submitted-2, 68ms, fix in case sum > 10

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def link(self, srcNode, nextNode):
        srcNode.next = nextNode
        return srcNode.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        main = ListNode(0)
        nextNode = main
        add = 0
        while True:
            x = l1.val
            y = l2.val
            sum = x + y + add
            fraction = sum % 10
            add = int(sum / 10)
            nextNode = self.link(nextNode, ListNode(fraction))
            if l1.next or l2.next or add > 0:
                l1 = l1.next or ListNode(0)
                l2 = l2.next or ListNode(0)  
            else:
                break
        return main.next
        