from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # Iterative
    # Time: O(n)
    # Space: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_tmp = curr.next
            curr.next = prev

            # Advance pointers
            prev = curr
            curr = next_tmp
        return prev

    # Recursive
    # Time: O(n)
    # Space: O(n) (Recursion Stack)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_head