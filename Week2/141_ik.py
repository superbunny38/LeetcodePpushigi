from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # Floyd's Cycle-Finding Algorithm
    # Tortoise and Hare algorithm
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = rabbit = head

        while rabbit and rabbit.next:
            tortoise = tortoise.next
            rabbit = rabbit.next.next
            if tortoise is rabbit:
                return True
        return False