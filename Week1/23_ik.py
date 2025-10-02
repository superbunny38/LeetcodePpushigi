# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Min Heap
    # Time: O(nlogk)
    # Space: O(k) (Heap에는 항상 K개만 들어감)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from heapq import heappush, heappop

        current = dummy = ListNode()
        heap = []

        # i는 동등비교 제거용
        for i, l in enumerate(lists):
            if l:
                heappush(heap, (l.val, i, l))

        while heap:
            val, i, node = heappop(heap)
            # Chained assignment
            # current = current.next = node 는 TLE 발생
            # node evaluate -> current = node -> current.next = node (잘못된 순서)
            # 즉 node.next = node가 되어버림 (자기 참조)
            current.next = node
            current = current.next

            if node.next:
                heappush(heap, (node.next.val, i, node.next))
        return dummy.next


    # Sequential merge
    # Time: O(nk) (한번 비교할 때 k개를 비교하고, N번의 비교 일어남)
    # Space: O(1)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeTwoLists(l1, l2):
            dummy = ListNode(0)
            current = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next

            current.next = l1 or l2
            return dummy.next

        # 하나씩 순차적으로 병합
        result = lists[0]
        for i in range(1, len(lists)):
            result = mergeTwoLists(result, lists[i])

        return result