
class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value= value
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_temp = curr.next   # 1. store next 
            curr.next = prev        # 2. reverse link
            prev = curr             # 3. move prev
            curr = next_temp        # 4. move curr

        return prev
   
def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    curr = head

    for value in values[1:]:
        curr.next = ListNode(value)
        curr = curr.next
    return head

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.value, end=" -> ")
        curr = curr.next
    print("None")   

values = [1, 2, 3, 4, 5]

# Create linked list
head = create_linked_list(values)
print("Original Linked List:")
print_linked_list(head)

# Reverse linked list
solution = Solution()
reversed_head = solution.reverseList(head)

print("Reversed Linked List:")
print_linked_list(reversed_head)
