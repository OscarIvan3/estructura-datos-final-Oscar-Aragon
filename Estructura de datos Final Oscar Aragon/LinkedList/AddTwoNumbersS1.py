class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class AddTwoNumbers:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            sum_ = carry
            if l1:
                sum_ += l1.val
                l1 = l1.next
            if l2:
                sum_ += l2.val
                l2 = l2.next

            carry = sum_ // 10
            current.next = ListNode(sum_ % 10)
            current = current.next

        return dummy.next

# Función para imprimir la lista
def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)