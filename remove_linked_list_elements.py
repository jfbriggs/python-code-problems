"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def removeElements(self, head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """


## TEST CODE ##

a = ListNode(4)
b = ListNode(1)
c = ListNode(2)
d = ListNode(7)
e = ListNode(2)
f = ListNode(9)
g = ListNode(12)
h = ListNode(3)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h

current = a
while current:
    print(current.val)
    current = current.next
