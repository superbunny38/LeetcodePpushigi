# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Recursion
    # 직관: 첫단계에서 더 작은 값을 가진 노드를 선택하고, 그 노드를 제외한 나머지와 다른 list들을 merge한 결과를 뒤에 이어붙이면 된다.
    # Time: O(n)
    # Space: O(n) (Recursion Stack)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


    # Dummy Node 사용
    # Time: O(n)
    # Space: O(1)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next
        current.next = list1 or list2
        return dummy.next

    # Min Heap 사용 (2 list에서는 비효율)
    # Time: O(nlogn)
    # Space: O(n)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        import heapq
        current = dummy = ListNode()
        heap = []

        while list1:
            heapq.heappush(heap, (list1.val, list1))
            list1 = list1.next
        while list2:
            heapq.heappush(heap, (list2.val, list2))
            list2 = list2.next

        while heap:
            val, node = heapq.heappop(heap)
            current = current.next = node

        return dummy.next
