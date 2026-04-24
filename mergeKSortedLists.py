class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []

        for node in lists:
            while node:
                values.append(node.val)
                node = node.next

        values.sort()
        
        dummy = ListNode(0)
        current = dummy

        for val in values:
            current.next = ListNode(val)
            current = current.next

        return dummy.next