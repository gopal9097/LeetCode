import heapq

class Solution:
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        current = dummy
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        while heap:
            val, i, node = heapq.heappop(heap)

            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next