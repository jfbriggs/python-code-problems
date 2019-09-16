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

def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """

    prev = None
    current = head

    while current:
        if current.val == val:
            if current == head:
                head = current.next
            else:
                prev.next = current.next
        else:
            prev = current
        current = current.next

    return head




#### TEST CODE ###

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

## Print the linked list in list form
def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    print(result)

print_linked_list(a)

## Remove a value from the Linked List and re-print
print_linked_list(removeElements(a, 2))
