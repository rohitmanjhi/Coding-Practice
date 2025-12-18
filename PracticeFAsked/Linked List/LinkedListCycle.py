class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# 🔴 NEW FUNCTION: linked list with cycle
def create_linked_list_with_cycle(values, pos):
    if not values:
        return None

    head = ListNode(values[0])
    curr = head
    cycle_node = None

    if pos == 0:
        cycle_node = head

    for i in range(1, len(values)):
        curr.next = ListNode(values[i])
        curr = curr.next

        if i == pos:
            cycle_node = curr

    # 🔴 yahin cycle create ho raha hai
    curr.next = cycle_node
    return head


# ------------------ TEST ------------------

values = [1, 2, 3, 4, 5, 6]
pos = 2   # index 2 => value 3

head = create_linked_list_with_cycle(values, pos)

print(has_cycle(head))   # ✅ True
