from typing_extensions import List


class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value= value
        self.next = next

class Solution(object):
    def mergeTwoList(self, list1, list2):

        dummy = ListNode(-1)
        tail = dummy

        while list1 and list2:
            if list1.value <= list2.value:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next        

        # Attach the remainig nodes
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next

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

list1 = [1, 3, 5]
list2 = [2, 4, 6]   

head1 = create_linked_list(list1)
head2 = create_linked_list(list2)

print_linked_list(head1)
print_linked_list(head2)

solution = Solution()

merge_head = solution.mergeTwoList(head1, head2)
print_linked_list(merge_head)
