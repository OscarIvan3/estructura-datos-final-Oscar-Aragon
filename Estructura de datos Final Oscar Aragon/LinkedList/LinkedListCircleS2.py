class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedListCycleSet:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        current = head

        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next

        return False
